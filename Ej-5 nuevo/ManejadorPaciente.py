#Modelo 2

class ManejadorPacientes:
    indice= 0
    __pacientes= None

    def __init__(self):
        self.__pacientes= []

    def agregarPaciente(self, paciente): #Recibe un paciente
        paciente.rowid= ManejadorPacientes.indice #Obtiene un indice de paciente y lo guarda en la variable "rowid"
        ManejadorPacientes.indice += 1
        self.__pacientes.append(paciente) #Agrega el paciente a la lista

    def getListaPacientes(self): #Devuelve todos los pacientes
        return self.__pacientes

    def deletePaciente(self, paciente): #Recibe un paciente y borra en la posición donde esté ese paciente
        indice= self.obtenerIndicePaciente(paciente) #Busca el índice del paciente
        self.__pacientes.pop(indice)

    def updatePaciente(self, paciente): #Recibe un paciente
        indice= self.obtenerIndicePaciente(paciente) #Obtiene el indice del paciente recibido
        self.__pacientes[indice]= paciente #Al paciente q está en ese indice le pone el nuevo valor


    def obtenerIndicePaciente(self, paciente): #Obtiene el índice del paciente, búsqueda normal
        bandera= False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera=True
            else:
                i+= 1
        return i


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__pacientes]
        )
        return d
