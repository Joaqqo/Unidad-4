

#Modelo 4

class RespositorioContactos(object):
    __conn= None
    __manejador= None


    def __init__(self, conn):
        self.__conn= conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)


    def to_values(self, paciente):
        return paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso()

    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()

    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente

    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
