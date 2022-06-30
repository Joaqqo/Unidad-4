

#Modelo 4

class RespositorioContactos(object): #RepositorioPaciente
    __conn= None #Conexión, (objectEncoder)
    __manejador= None #ManejadorPaciente

#Se crea este repositorio porque cambiando algunas cosas de aca, se puede pasar a base de datos
#Es decir representa el almacenamiento
#Pasa a un archivo a JSON pero puede irse a cualquier otra base de datos
    def __init__(self, conn):
        self.__conn= conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)


    def to_values(self, paciente):
        return paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso()
#Ejecutan los métodos del manejador
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente #Devuelve pq va a parar a una parte de la "Vista"

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()

    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente #Devuelve pq va a parar a una parte de la "Vista"

    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
