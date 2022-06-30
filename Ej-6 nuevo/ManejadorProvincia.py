#Modelo 2
class ManejadorProvincias:
    __provincias= None

    def __init__(self):
        self.__provincias= []

    def agregarProvincia(self, provincia): #Recibe un paciente
        self.__provincias.append(provincia)#Agrega el paciente a la lista

    def getListaProvincias(self):#Devuelve todos los pacientes
        return self.__provincias

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON() for provincia in self.__provincias]
        )
        return d
