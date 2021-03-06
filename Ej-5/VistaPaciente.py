import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from Paciente import Paciente

#--------------------------------------------------------------------------------------------------
class PatientList(tk.Frame): #Vista 1 (Es la lista con los nombres del costado a la izquierda)
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, paciente, index=tk.END):
        text= "{}, {}".format(paciente.getApellido(), paciente.getNombre())
        self.lb.insert(index,text)

    def borrar(self, index):
        self.lb.delete(index,index)

    def modificar(self, contact, index):
        self.borrar(index)
        self.insertar(contact, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

#--------------------------------------------------------------------------------------------------
class PatientForm(tk.LabelFrame): #Vista 2 (Es el "formato")
    fields= ("Apellido", "Nombre", "Telefono", "Altura", "Peso")

    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text= field
        label= tk.Label(self.frame, text=text)
        entry= tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoPacienteEnFormulario(self, paciente):
        values = (paciente.getApellido(), paciente.getNombre(),
                  paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearContactoDesdeFormulario(self):
        values= [e.get() for e in self.entries]
        paciente= None
        try:
            paciente= Paciente(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validaci??n", str(e), parent=self)
        return paciente

    def Limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

#--------------------------------------------------------------------------------------------------
class NewPatient(tk.Toplevel): #Vista 3 (Para confirmar un nuevo paciente)
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente= None
        self.form= PatientForm(self)
        self.btn_add= tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.paciente= self.form.crearContactoDesdeFormulario()
        if self.paciente:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente

#--------------------------------------------------------------------------------------------------
class UpdatePatientForm(PatientForm): #Vista 3 (Para actualizar el formulario de los pacientes)
#ya sea guardando un paciente nuevo, borrando uno o mostrando el IMC de un paciente
    __imc= None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__imc = StringVar()
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_imc = tk.Button(self, text="Ver IMC")
        self.btn_imc.pack(side=tk.LEFT, ipadx=5, padx=5, pady=5)
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_imc(self, callback):
        self.btn_imc.config(command=callback)
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

#--------------------------------------------------------------------------------------------------
class PatientsView(tk.Tk): #Vista 4 (La parte "est??tica" del programa)
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = PatientList(self, height=15)
        self.form = UpdatePatientForm(self)
        self.btn_new = tk.Button(self, text="Agregar paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self,ctrl):
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_imc(ctrl.IMC)

    def IMC(self,lista):
        self.altura = StringVar()
        self.peso = StringVar()
        self.peso.set(lista[0])
        self.altura.set(lista[1])
        self.nuevo = Toplevel()
        self.nuevo.geometry("300x150")
        self.nuevo.resizable(0, 0)
        self.nuevo.title("IMC")
        self.IMCLabel = ttk.Label(self.nuevo, text="IMC", padding=(5, 5))
        self.PesoCorporalLabel = ttk.Label(self.nuevo, text="Composici??n Corporal", padding=(5, 5))
        self.PesoEntry = ttk.Entry(self.nuevo, textvariable=self.peso, width=21, justify="left")
        self.AlturaEntry = ttk.Entry(self.nuevo, textvariable=self.altura, width=21, justify="left")
        self.VolverBoton = Button(self.nuevo, text="Volver", padx=5, pady=5, command=self.nuevo.destroy)
        self.IMCLabel.place(x=40, y=30)
        self.PesoCorporalLabel.place(x=0, y=60)
        self.PesoEntry.place(x=135, y=35)
        self.AlturaEntry.place(x=135, y=65)
        self.VolverBoton.place(x=130, y=105)

    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)

    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente,index)

    def borrarPaciente(self, index):
        self.form.Limpiar()
        self.list.borrar(index)

    def obtenerDetalles(self):
        return self.form.crearContactoDesdeFormulario()

    def verPacienteEnForm(self, contacto):
        self.form.mostrarEstadoPacienteEnFormulario(contacto)
