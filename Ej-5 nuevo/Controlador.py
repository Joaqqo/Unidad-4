from VistaPaciente import PatientsView, NewPatient


#Controlador 1

class ControladorPacientes(object): #Clase que deriva de object
    def __init__(self, repo, vista):
        self.repo= repo #Repositorio
        self.vista= vista #Vista
        self.seleccion= -1 #Selección -1 para que no haya ninguno seleccionado en el listbox
        self.pacientes= list(repo.obtenerListaPacientes()) #Obtiene la lista de los pacientes a partir del repositorio (el q tiene el acceso a json)

    #comandos que se ejecutan a través de la vista

    def crearPaciente(self):
        nuevoPaciente= NewPatient(self.vista).show() #Invocación a newpatient
        if nuevoPaciente: #Si obtuvo un paciente nuevo
            paciente= self.repo.agregarPaciente(nuevoPaciente) #Lo agrega
            self.pacientes.append(paciente) #Lo agrega a la lista
            self.vista.agregarPaciente(paciente) #Lo muestra

    def seleccionarPaciente(self, index): #Obtiene el indice
        self.seleccion= index
        paciente= self.pacientes[index] #Paciente que hay en el indice indicado
        self.vista.verPacienteEnForm(paciente) #Lo muestra en el formulario de la derecha

    def modificarPaciente(self): #Modifica paciente
        if self.seleccion == -1: #Valida primero si no hay nadie seleccionado
            return #Si está en -1 se sale de la función
        rowid = self.pacientes[self.seleccion].rowid #Sino obtiene el rowid que es la posición dentro de la lista de pacientes
        detallesPaciente = self.vista.obtenerDetalles() #Obtiene los datos del paciente
        detallesPaciente.rowid = rowid #Le establece el rowid que había obtenido
        contacto = self.repo.modificarPaciente(detallesPaciente) #Modifica el contacto con los datos del paciente obtenido
        self.pacientes[self.seleccion] = contacto
        self.vista.modificarPaciente(contacto, self.seleccion)
        self.seleccion = -1 #Ya dejó de estar seleccionado, entonces lo vuelve a poner en -1

    def borrarPaciente(self):
        if self.seleccion == -1: #Valida primero si no hay nadie seleccionado
            return #Si está en -1 se sale de la función
        paciente = self.pacientes[self.seleccion] #Si está seleccionado, obtiene el contacto
        self.repo.borrarPaciente(paciente) #Borra del repositorio
        self.pacientes.pop(self.seleccion) #Borra de la lista de pacientes
        self.vista.borrarPaciente(self.seleccion) #Borra el paciente q fue seleccionado del listbox
        self.seleccion = -1 #Ya dejó de estar seleccionado, entonces lo vuelve a poner en -1

    def IMC(self): #Cálculos para sacar el IMC
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        valor1 = float(paciente.getAltura()) / 100
        valor2 = float(paciente.getPeso())
        valorfinal = valor2 / (valor1 * valor1)
        if valorfinal < 18.5:
            mensaje = "Peso inferior al normal"
        elif valorfinal < 24.9:
            mensaje = "Peso Normal"
        elif valorfinal < 29.9:
            mensaje = "Peso superior al normal"
        else:
            mensaje = "Obesidad"
        valorfinal = round(valorfinal, 2)
        lista = [valorfinal, mensaje]
        self.vista.IMC(lista)

    def start(self): #Ejecuta la vista, (la ventana)
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()

    def salirGrabarDatos(self): #Método de grabar datos para que cuando salga siempre se graben los datos
        self.repo.grabarDatos()
