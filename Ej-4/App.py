from tkinter import *
from tkinter import ttk
from functools import partial
from Fraccion import Fraccion


class App:
    __Ventana = None
    __operador = None
    __panel = None
    __operadorAux = None
    __primerOperando = None #numeros
    __segundoOperando = None #numeros

    def __init__(self):
        self.__Ventana = Tk()
        self.__Ventana.title("Tk-Calculadora")
        mainframe = ttk.Frame(self.__Ventana, padding="3 10 3 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        EntryOperador = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        EntryOperador.grid(column=1, row=1, columnspan=1, sticky=(W, E))
        EntryPanel = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        EntryPanel.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerNUMERO, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, text='<-', command=partial(self.borrarencero)).grid(column=3, row=8, sticky=W)
        self.__panel.set("0")
        EntryPanel.focus()
        self.__Ventana.mainloop()

    def ponerNUMERO(self, numero): #Para mostrar el número
        if self.__operadorAux is None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero) #Para que se vean juntos los numeros
        else: #Segunda pasada, entra por aca
            self.__operadorAux = None
            valor = self.__panel.get()
            self.__primerOperando = valor
            self.__panel.set(numero)

    def borrarencero(self):
        self.__panel.set("0")

    def Resuelve(self, op1, op2, operacion): #Resuelve, y en caso de ser de clase fracción está la sobrecarga de operadores
        resultado=None
        if operacion == '+':
            resultado = op1 + op2
        else:
            if operacion == '-':
                resultado = op1 - op2
            else:
                if operacion == '*':
                    resultado = op1 * op2
                else:
                    if operacion == '%':
                        resultado = op1 / op2
        return resultado

    def resolverOperacion(self, operando1, operacion, operando2): #Para resolver la fracción
        if operando1.find("/") == -1 and operando2.find("/") == -1: #-1 significa que no encontró el '/', es decir hace el cálculo "normal"
            op1 = int(operando1)
            op2 = int(operando2)
            result = self.Resuelve(op1, op2, operacion)  #Manda a la función resuelve que haga el cálculo de suma, resta, multiplicación o división
        else:
            op1 = operando1.split("/") #Divide los números, es decir si vino un 1/2 lo divide en 1 y en 2
            op2 = operando2.split("/")

            try:
                op1 = Fraccion(int(op1[0]), int(op1[1])) #Entonces se "lleva" los primeros operandos
            finally:
                op2 = Fraccion(int(op2[0]), int(op2[1])) #Y después se "lleva" los otros dos números
            result = self.Resuelve(op1, op2, operacion)
        self.__panel.set(str(result))

    def ponerOPERADOR(self, op): #Para mostrar el operador
        if op == '=': #Cuando el operador sea =
            operacion = self.__operador.get() #Obtenemos el operador
            self.__segundoOperando = self.__panel.get() #Segundo operando
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando) #Resolvemos la operacion
            self.__operador.set("")
            self.__operadorAux = None
        else:
            if self.__operador.get() == "":
                self.__operador.set(op) #Setear el operador que llega
                self.__operadorAux = op #Y ponerle el mismo al operador auxiliar
