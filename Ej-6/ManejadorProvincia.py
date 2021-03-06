#Modelo 2
class ManejadorProvincias:
    __provincias= None

    def __init__(self):
        self.__provincias= []

    def agregarProvincia(self, provincia):
        self.__provincias.append(provincia)

    def getListaProvincias(self):
        return self.__provincias

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON() for provincia in self.__provincias]
        )
        return d
