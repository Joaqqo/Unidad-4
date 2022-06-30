import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from Paciente import Paciente

#--------------------------------------------------------------------------------------------------
#Vista 1 (Es "listbox" donde se muestran los pacientes a la izquierda)
class PatientList(tk.Frame): #Clase q deriva de tk.Frame
    def __init__(self, master, **kwargs): #Init que recibe la ventana maestra y kwargs
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs) #Agrega el listbox con los argumentos q recibe
        scroll = tk.Scrollbar(self, command=self.lb.yview) #Barra de scroll e invocación al método yview de las listas para poder verlas
        self.lb.config(yscrollcommand=scroll.set) #Config q establece la barra de scroll
        scroll.pack(side=tk.RIGHT, fill=tk.Y) #Geometría pack para ubicar todo
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, paciente, index=tk.END): #Recibe un paciente y por defecto lo ubica al final, si le damos un índice lo pone en ese lugar
        text= "{}, {}".format(paciente.getApellido(), paciente.getNombre()) #Arma un texto con el apellido y nombre del paciente
        self.lb.insert(index,text) #Lo inserta en la lista

    def borrar(self, index):
        self.lb.delete(index,index) #Borrar del índice q recibe

    def modificar(self, contact, index): #Borra el paciente indicado en el indice e inserta el nuevo
        self.borrar(index)
        self.insertar(contact, index)

    def bind_doble_click(self, callback): #Doble click para seleccionar un contacto
        handler = lambda _: callback(self.lb.curselection()[0]) #Curse selection, selección actual
        self.lb.bind("<Double-Button-1>", handler)

#--------------------------------------------------------------------------------------------------
#Vista 2 (Es el "formato", como vemos los datos de la lista de la derecha)
class PatientForm(tk.LabelFrame):
    fields= ("Apellido", "Nombre", "Telefono", "Altura", "Peso") #Campos

    def __init__(self, master, **kwargs): #Parámetros tal cual lo reciben
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs) #Master es donde se muestra
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields))) #Hace un mapeo con crearCampo y la enumeración de los campos de fields
        #Esto lo que hace es que va a crear una entry para todos los datos de fields (Apellido, Nombre, etc)
        self.frame.pack()

    def crearCampo(self, field): #Recibe el campo que tiene que crear (field) y pone el label, y el entry
        position, text= field
        label= tk.Label(self.frame, text=text)
        entry= tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5) #Geometría grid
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoPacienteEnFormulario(self, paciente): #Recibe un paciente y hace la recuperación de los valores que se ven ahí
        values = (paciente.getApellido(), paciente.getNombre(),
                  paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values): #Recorre las entry's del formulario q acabamos de crear
            entry.delete(0, tk.END) #Los borra
            entry.insert(0, value) #Inserta el valor que recuperamos
#Básicamente cuando seleccionamos un paciente de la izquierda, se tiene que reflejar en la derecha
    def crearContactoDesdeFormulario(self): #Desde los entrys que tenemos, creamos un objeto Paciente
        values= [e.get() for e in self.entries] #Para cada uno de los elementos que hay en entries, los recupera
        paciente= None
        try:
            paciente= Paciente(*values) #Genera un objeto paciente con los valores
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return paciente

    def Limpiar(self): #Recorre las entries y las va borrando
        for entry in self.entries:
            entry.delete(0, tk.END)

#--------------------------------------------------------------------------------------------------
#Vista 3 (Para confirmar un nuevo paciente)
class NewPatient(tk.Toplevel): #Paciente nuevo, crea un formulario add que deriva de TopLevel
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente= None #Crea objeto paciente con None
        self.form= PatientForm(self) #Crea formulario
        self.btn_add= tk.Button(self, text="Confirmar", command=self.confirmar) #Botón confirmar
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self): #Cuando se le dé al botón confirmar
        self.paciente= self.form.crearContactoDesdeFormulario() #Crea contactodesde formulario (Vista 2)
        if self.paciente: #Si obtuvo un contacto, destruye el formulario
            self.destroy()

    def show(self): #Lo muestra con show()
        self.grab_set() #Abre el formulario y espera a que uno ingrese los datos
        self.wait_window()
        return self.paciente

#--------------------------------------------------------------------------------------------------
#Vista 3 (Para actualizar el formulario de los pacientes)
class UpdatePatientForm(PatientForm): #Deriva de PatientForm de la vista 2
#ya sea guardando un paciente nuevo, borrando uno o mostrando el IMC de un paciente
    __imc= None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__imc = StringVar()
        self.btn_save = tk.Button(self, text="Guardar") #Botón para guardar
        self.btn_delete = tk.Button(self, text="Borrar") #Botón para borrar
        self.btn_imc = tk.Button(self, text="Ver IMC")
        self.btn_imc.pack(side=tk.LEFT, ipadx=5, padx=5, pady=5)
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_imc(self, callback):
        self.btn_imc.config(command=callback)
    def bind_save(self, callback): #Bind save para guardar, lo deja para después con el callback
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
#Usa el callback pq los maneja el controlador
#--------------------------------------------------------------------------------------------------
#Vista 4 (La parte "estética" del programa)
class PatientsView(tk.Tk):  #Este es el que integra TODO
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes") #Título
        self.list = PatientList(self, height=15)  #Lista de pacientes (Vista 1)
        self.form = UpdatePatientForm(self) #Formulario de vista 3 con borrar y guardar
        self.btn_new = tk.Button(self, text="Agregar paciente") #Botón para agregar paciente
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self,ctrl): #Como es la vista tiene que establecerse quien es el controlador y que es lo que va a hacer
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente) #Métodos pendientes que dejamos en vista 3
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_imc(ctrl.IMC)
#Vincula la vista con el controlador el setControlador, recibe el controlador (ctrl)
    def IMC(self,lista): #Lo de IMC
        self.altura = StringVar()
        self.peso = StringVar()
        self.peso.set(lista[0])
        self.altura.set(lista[1])
        self.nuevo = Toplevel()
        self.nuevo.geometry("300x150")
        self.nuevo.resizable(0, 0)
        self.nuevo.title("IMC")
        self.IMCLabel = ttk.Label(self.nuevo, text="IMC", padding=(5, 5))
        self.PesoCorporalLabel = ttk.Label(self.nuevo, text="Composición Corporal", padding=(5, 5))
        self.PesoEntry = ttk.Entry(self.nuevo, textvariable=self.peso, width=21, justify="left")
        self.AlturaEntry = ttk.Entry(self.nuevo, textvariable=self.altura, width=21, justify="left")
        self.VolverBoton = Button(self.nuevo, text="Volver", padx=5, pady=5, command=self.nuevo.destroy)
        self.IMCLabel.place(x=40, y=30)
        self.PesoCorporalLabel.place(x=0, y=60)
        self.PesoEntry.place(x=135, y=35)
        self.AlturaEntry.place(x=135, y=65)
        self.VolverBoton.place(x=130, y=105)

    def agregarPaciente(self, paciente): #Agrega paciente
        self.list.insertar(paciente) #list es el contact list que está al principio

    def modificarPaciente(self, paciente, index): #Modifica paciente
        self.list.modificar(paciente,index)

    def borrarPaciente(self, index): #Borra paciente
        self.form.Limpiar()
        self.list.borrar(index)

    def obtenerDetalles(self): #Crea un paciente desde el formulario
        return self.form.crearContactoDesdeFormulario()

    def verPacienteEnForm(self, contacto): #Muestra un paciente que ha sido seleccionado a partir de la lista
        self.form.mostrarEstadoPacienteEnFormulario(contacto)
