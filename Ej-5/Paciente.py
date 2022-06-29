import re
#Modelo 1
class Paciente:
    __nombre= ""
    __apellido= ""
    __telefono= ""
    __altura= ""
    __peso= ""

    def __init__(self, apellido, nombre, telefono, altura, peso):
        self.__nombre= self.verificador(nombre, "Nombre es un valor requerido")
        self.__apellido= self.verificador(apellido, "Apellido es un valor requerido")
        self.__telefono= self.verificadorTelefono(telefono, "Telefono no tiene formato correcto")
        self.__altura= self.verificadorAltuPeso(altura, "Altura no tiene formato correcto")
        self.__peso= self.verificadorAltuPeso(peso, "Peso no tiene formato correcto")

    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso


    def verificador(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def verificadorTelefono(self, valor, mensaje):
        if not valor or not re.match(r"\([0-9]{3}\)[0-9]{7}", valor):
            raise ValueError(mensaje)
        return valor

    def verificadorAltuPeso(self, valor, mensaje):
        if not valor or not re.match("^[0-9]{1,3}$", valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                apellido=self.__apellido,
                nombre=self.__nombre,
                telefono=self.__telefono,
                altura=self.__altura,
                peso=self.__peso
            )
        )
        return d
