import tkinter as tk
from tkinter import messagebox
from Provincia import Provincia

#--------------------------------------------------------------------------------------------------
class ProvinciasList(tk.Frame):#Vista 1 (Es la lista con los nombres del costado a la izquierda)
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END):
        text= "{}" .format(provincia.getNombre().title())
        self.lb.insert(index,text)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

#--------------------------------------------------------------------------------------------------
class ProvinciasForm(tk.LabelFrame): #Vista 2 (Es el "formato")
    fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos", "Temperatura", "Sensación térmica", "Humedad")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        if type(master) == NewProvincia:
            self.fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos")
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        values = (provincia.getNombre().title(), provincia.getCapital().title(),
                  provincia.getHabitantes(), provincia.getDepartamentos(),
                  provincia.getTemperatura(), provincia.getSensacionTermica(), provincia.getHumedad())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearProvinciaDesdeFormulario(self):
        rvalues = []
        values = [e.get() for e in self.entries]
        for i in range(4):
            rvalues.append(values[i])
        provincia = None
        try:
            provincia = Provincia(*rvalues)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

#--------------------------------------------------------------------------------------------------
class NewProvincia(tk.Toplevel):#Vista 3 (Para confirmar una nueva provincia)
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = ProvinciasForm(self)
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

#--------------------------------------------------------------------------------------------------
class ProvinciasView(tk.Tk): #Vista 4 (La parte "estética" del programa)
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.list = ProvinciasList(self, height=15)
        self.form = ProvinciasForm(self)
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)

    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)

    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()

    def verProvinciaEnForm(self, p):
        self.form.mostrarEstadoProvinciaEnFormulario(p)
