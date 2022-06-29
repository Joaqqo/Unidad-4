class Fraccion:
    __numerador = 0
    __denominador = 0

    def __init__(self, num, den=1):
        self.__numerador = num
        self.__denominador = den
    def __str__(self):
         return f"numerador: {self.__numerador} denominador: {self.__denominador}"


    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador

    def __add__(self, otro):
        numerador = self.__numerador * otro.getDenominador() + self.__denominador * otro.getNumerador()
        denominador = self.__denominador * otro.getDenominador()
        return self.simplificar(numerador, denominador)

    def __sub__(self, otro):
        numerador = self.__numerador * otro.getDenominador() - self.__denominador * otro.getNumerador()
        denominador = self.__denominador * otro.getDenominador()
        return self.simplificar(numerador, denominador)

    def __mul__(self, otro):
        numerador = self.__numerador * otro.getNumerador()
        denominador = self.__denominador * otro.getDenominador()
        return self.simplificar(numerador, denominador)

    def __truediv__(self, otro):
        numerador = self.__numerador * otro.getDenominador()
        denominador = self.__denominador * otro.getNumerador()
        return self.simplificar(numerador, denominador)

    def simplificar(self, n, d):
        bandera = False
        if n != d:
            z = max(n, d) #Devuelve el num mayor
            while not bandera:
                if z % n == 0 and z % d == 0:
                    bandera = True
                else:
                    z += 1
            n = z // n  #"Floor division" resultado un num entero
            d = z // d
            if n == 1:
                resultado = str(d) #Lo transforma en string
            else:
                resultado = "{}/{}".format(d, n)
        else:
            resultado = "1"
        return resultado
