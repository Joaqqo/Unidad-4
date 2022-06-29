from tkinter import ttk, Tk, StringVar, messagebox
from tkinter.constants import *
import requests

class App:
    __ventana= None
    __valDolar= None
    __valPesos= None


    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title("Conversor de moneda")
        self.__ventana.resizable(0,0)
        self.__valDolar= StringVar()
        self.__valPesos= StringVar()
        self.__valDolar.trace("w", self.CalculaDolar)


        #---Creación de frame, labels, botones---

        frame= ttk.Frame(self.__ventana, width=290, height=115)
        #-----------------------------------------------------------------------
        self.EntryDolar= ttk.Entry(frame, textvariable=self.__valDolar, width=7)
        #-----------------------------------------------------------------------
        self.LabelDolar= ttk.Label(frame, text="dólares", padding=(5,5))
        self.LabelPesos= ttk.Label(frame, text="pesos", padding=(5,5))
        self.LabelEquiv= ttk.Label(frame, text="es equivalente a", padding=(5,5))
        self.LabelMostrar= ttk.Label(frame, textvariable=self.__valPesos, padding=(5,5))
        #-----------------------------------------------------------------------
        self.BotonSalir= ttk.Button(frame, text="Salir", command=self.__ventana.destroy)


        #--Posicionamiento de frame, labels, botones---


        frame.place(x=0, y=0)
        self.EntryDolar.place(x=150, y=15)
        self.LabelDolar.place(x=200, y=12)
        self.LabelPesos.place(x=200, y=45)
        self.LabelEquiv.place(x=35, y=45)
        self.LabelMostrar.place(x=140, y=45)
        self.BotonSalir.place(x=200, y=70)
        self.__ventana.mainloop()


    def CalculaDolar(self, *args): #Busca el valor del dolar en la página y hace la conversión
        url= "https://www.dolarsi.com/api/api.php?type=dolar"
        r= requests.get(url)
        valor= r.json() #Convierte a json
        valor= valor[0] #Trae "todo"
        valor= valor["casa"]["venta"] #Trae el valor del dólar Oficial para la venta
        valor= valor.split(",") #Lo divide con la coma para después poder separarlo con un punto
        if self.__valDolar.get() != "":
            try:
                dolar= float(self.__valDolar.get())
                self.__valPesos.set(valor[0] + "." + valor[1])
                pesos= float(self.__valPesos.get())
                self.__valPesos.set(round(float(pesos)*float(dolar), 2)) #Redondea a un número con 2 decimales
            except: #En caso de que se ingrese un valor incorrecto, saldrá este error 
                messagebox.showerror(title="Error Valor", message="Ingrese un número correcto por favor.")
                self.__valDolar.set("")
                self.__EntryDolar.focus()
        else:
            self.__valPesos.set("")
