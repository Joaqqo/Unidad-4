import requests
#Modelo 1
class Provincia:
    __nombre= ""
    __capital= ""
    __habitantes= ""
    __departamentos= ""



    def __init__(self, nombre, capital, habitantes, departamentos):
        self.__nombre= self.verificadorNombre(nombre, "Nombre inválido de provincia")
        self.__capital= self.verificador(capital, "Capital es un valor requerido")
        self.__habitantes= self.verificador(habitantes, "Habitantes es un valor requerido")
        self.__departamentos= self.verificador(departamentos, "Departamentos es un valor requerido")

    def obtenerJson(self, p):
        complete_url = "https://api.openweathermap.org/data/2.5/weather?q=" + p.lower() + "&units=metric&appid=55a81b14e1d058728bc865b70b6569d2" #P.lower es el nombre de la provincia para tener la URL completa
        r = requests.get(complete_url)
        v = r.json()
        return v

    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getHabitantes(self):
        return self.__habitantes
    def getDepartamentos(self):
        return self.__departamentos


    def getTemperatura(self):
        valor=self.obtenerJson(self.__nombre)
        return valor["main"]["temp"]
    def getSensacionTermica(self):
        valor= self.obtenerJson(self.__nombre)
        return valor["main"]["feels_like"]
    def getHumedad(self):
        valor= self.obtenerJson(self.__nombre)
        return valor["main"]["humidity"]



    def verificador(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor


    def verificadorNombre(self, valor, mensaje):
        v= self.obtenerJson(valor)
        try:
            v["main"]
        except:
            raise ValueError(mensaje)
        return valor


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                nombre=self.__nombre,
                capital=self.__capital,
                habitantes=self.__habitantes,
                departamentos=self.__departamentos
            )
        )
        return d
