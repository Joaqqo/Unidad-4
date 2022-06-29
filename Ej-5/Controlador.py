from VistaPaciente import PatientsView, NewPatient


#Controlador 1

class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo= repo
        self.vista= vista
        self.seleccion= -1
        self.pacientes= list(repo.obtenerListaPacientes())

    #comandos que se ejecutan a través de la vista

    def crearPaciente(self):
        nuevoPaciente= NewPatient(self.vista).show()
        if nuevoPaciente:
            paciente= self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)

    def seleccionarPaciente(self, index):
        self.seleccion= index
        paciente= self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)

    def modificarPaciente(self):
        if self.seleccion == -1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        contacto = self.repo.modificarPaciente(detallesPaciente)
        self.pacientes[self.seleccion] = contacto
        self.vista.modificarPaciente(contacto, self.seleccion)
        self.seleccion = -1

    def borrarPaciente(self):
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion = -1

    def IMC(self):
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

    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()
