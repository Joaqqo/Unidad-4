#Modelo 4

class RepositorioProvincia(object): #RepositorioPaciente
    __conn= None #Conexión, (objectEncoder)
    __manejador= None #ManejadorPaciente
#Se crea este repositorio porque cambiando algunas cosas de aca, se puede pasar a base de datos
#Es decir representa el almacenamiento
#Pasa a un archivo a JSON pero puede irse a cualquier otra base de datos

    def __init__(self, conn):
        self.__conn= conn
        diccionario= self.__conn.leerJSONArchivo()
        self.__manejador= self.__conn.decodificarDiccionario(diccionario)


    def to_values(self, provincia):
        return provincia.getNombre(), provincia.getCapital(), provincia.getHabitantes(), provincia.getDepartamentos()
#Ejecutan los métodos del manejador
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()

    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia #Devuelve pq va a parar a una parte de la "Vista"

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
