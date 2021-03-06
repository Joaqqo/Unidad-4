import json
from pathlib import Path
from ManejadorProvincia import ManejadorProvincias
from Provincia import Provincia

#Modelo 3

class Decodificador(object):
    __nombreArchivo = None

    def __init__(self, archivo):
        self.__nombreArchivo = archivo

    def decodificarDiccionario(self, d):
        manejador=None
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'ManejadorProvincias':
                provincias = d['provincias']
                manejador = class_()
                for i in range(len(provincias)):
                    dProvincia = provincias[i]
                    class_name = dProvincia.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dProvincia['__atributos__']
                    unaProvincia = class_(**atributos)
                    manejador.agregarProvincia(unaProvincia)
            return manejador

    def guardarJSONArchivo(self, diccionario):
        with Path(self.__nombreArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__nombreArchivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
