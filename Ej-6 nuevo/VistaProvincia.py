import tkinter as tk
from tkinter import messagebox
from Provincia import Provincia

#--------------------------------------------------------------------------------------------------
#Vista 1 (Es "listbox" donde se muestran los pacientes a la izquierda)
class ProvinciasList(tk.Frame):#Clase q deriva de tk.Frame
    def __init__(self, master, **kwargs): #Init que recibe la ventana maestra y kwargs
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs) #Agrega el listbox con los argumentos q recibe
        scroll = tk.Scrollbar(self, command=self.lb.yview)#Barra de scroll e invocación al método yview de las listas para poder verlas
        self.lb.config(yscrollcommand=scroll.set)#Config q establece la barra de scroll
        scroll.pack(side=tk.RIGHT, fill=tk.Y)#Geometría pack para ubicar todo
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END): #Recibe un paciente y por defecto lo ubica al final, si le damos un índice lo pone en ese lugar
        text= "{}" .format(provincia.getNombre().title()) #Arma un texto con el nombre de la provincia
        self.lb.insert(index,text)

    def bind_doble_click(self, callback): #Doble click para seleccionar un contacto
        handler = lambda _: callback(self.lb.curselection()[0]) #Curse selection, selección actual
        self.lb.bind("<Double-Button-1>", handler)

#--------------------------------------------------------------------------------------------------
#Vista 2 (Es el "formato", como vemos los datos de la lista de la derecha)
class ProvinciasForm(tk.LabelFrame): #Vista 2 (Es el "formato")
    fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos", "Temperatura", "Sensación térmica", "Humedad") #Campos

    def __init__(self, master, **kwargs): #Parámetros tal cual lo reciben
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs) #Master es donde se muestra
        if type(master) == NewProvincia:
            self.fields = ("Nombre", "Capital", "Cantidad de habitantes", "Cantidad de departamentos/partidos")
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields))) #Hace un mapeo con crearCampo y la enumeración de los campos de fields
        self.frame.pack()

    def crearCampo(self, field): #Recibe el campo que tiene que crear (field) y pone el label, y el entry
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5) #Geometría grid
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia): #Recibe una provincia y hace la recuperación de los valores que se ven ahí
        values = (provincia.getNombre().title(), provincia.getCapital().title(),
                  provincia.getHabitantes(), provincia.getDepartamentos(),
                  provincia.getTemperatura(), provincia.getSensacionTermica(), provincia.getHumedad())
        for entry, value in zip(self.entries, values): #Recorre las entry's del formulario q acabamos de crear
            entry.delete(0, tk.END) #Los borra
            entry.insert(0, value) #Inserta el valor que recuperamos
#Básicamente cuando seleccionamos un paciente de la izquierda, se tiene que reflejar en la derecha
    def crearProvinciaDesdeFormulario(self): #Desde los entrys que tenemos, creamos un objeto Provincia
        rvalues = []
        values = [e.get() for e in self.entries] #Para cada uno de los elementos que hay en entries, los recupera
        for i in range(4):
            rvalues.append(values[i])
        provincia = None
        try:
            provincia = Provincia(*rvalues) #Genera un objeto provincia con los valores
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self): #Recorre las entries y las va borrando
        for entry in self.entries:
            entry.delete(0, tk.END)

#--------------------------------------------------------------------------------------------------
#Vista 3 (Para confirmar una nueva provincia)
class NewProvincia(tk.Toplevel):#Provincia nueva, crea un formulario add que deriva de TopLevel
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None #Crea objeto provincia con None
        self.form = ProvinciasForm(self) #Crea formulario
        self.btn_add = tk.Button(self, text="Confirmar", command=self.confirmar) #Botón confirmar
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self): #Cuando se le dé al botón confirmar
        self.provincia = self.form.crearProvinciaDesdeFormulario() #Crea contactodesde formulario (Vista 2)
        if self.provincia: #Si obtuvo un contacto, destruye el formulario
            self.destroy()

    def show(self): #Lo muestra con show()
        self.grab_set() #Abre el formulario y espera a que uno ingrese los datos
        self.wait_window()
        return self.provincia

#--------------------------------------------------------------------------------------------------
#Vista 4 (La parte "estética" del programa)
class ProvinciasView(tk.Tk): #Este es el que integra TODO
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias") #Título
        self.list = ProvinciasList(self, height=15) #Lista de provincias (Vista 1)
        self.form = ProvinciasForm(self) #Formulario de vista 3 con borrar y guardar
        self.btn_new = tk.Button(self, text="Agregar Provincia") #Botón para agregar provincia
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl): #Como es la vista tiene que establecerse quien es el controlador y que es lo que va a hacer
        self.btn_new.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)
#Vincula la vista con el controlador el setControlador, recibe el controlador (ctrl)
    def agregarProvincia(self, provincia): #Agrega provincia
        self.list.insertar(provincia) #list es el contact list que está al principio

    def obtenerDetalles(self):  #Crea una provincia desde el formulario
        return self.form.crearProvinciaDesdeFormulario()

    def verProvinciaEnForm(self, p): #Muestra una provincia que ha sido seleccionado a partir de la lista
        self.form.mostrarEstadoProvinciaEnFormulario(p)
