from tkinter import *
from tkinter import ttk, font, messagebox


class App:
    __ventana= None
    __pesokg= None
    __estatura= None
    __IMC=None
    __pesokgFinal= None

    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.title("Calculadora de IMC")
        self.__ventana.geometry("700x350")
        self.__ventana.resizable(0, 0)
        Titulo= font.Font(weight="normal", size=17) #Formato para el título
        Texto= font.Font(size=11) #Formato para el texto
        TextoenNegrita= font.Font(size=11, weight="normal") #Formato para el texto en negrita


        #---Creación de entrys, botones, separadores, labels---

        self.mensajePrincipal= ttk.Label(self.__ventana, text="Calculadora de IMC", font=Titulo, padding=(5,5))
        self.__pesokg= StringVar()
        self.__estatura= StringVar()
        self.__IMC= DoubleVar()
        self.__pesokgFinal= StringVar()
        #----------------------------------------------------------------------------------------
        self.separador1= ttk.Separator(self.__ventana, orient=HORIZONTAL)
        self.separador2= ttk.Separator(self.__ventana, orient=HORIZONTAL)
        self.separador3= ttk.Separator(self.__ventana, orient=HORIZONTAL)
        #----------------------------------------------------------------------------------------
        self.labelEstatura= ttk.Label(self.__ventana, text="Altura:", font=Texto, padding=(5,5))
        self.labelPeso= ttk.Label(self.__ventana, text="Peso:", font=Texto, padding=(5,5))
        self.labelCM= ttk.Label(self.__ventana, text="cm", font=Texto, background="#A8ADA8", padding=(3,1))
        self.labelKG= ttk.Label(self.__ventana, text="kg", font=Texto, background="#A8ADA8", padding=(3,1))
        #----------------------------------------------------------------------------------------
        self.EntryKG= ttk.Entry(self.__ventana, textvariable= self.__pesokg, width= 65)
        self.EntryEst= ttk.Entry(self.__ventana, textvariable= self.__estatura, width= 65)
        #----------------------------------------------------------------------------------------
        self.boton1= Button(self.__ventana, text="Calcular", padx=55, pady=5, background="#21A118", foreground="white", command=self.Calcular)
        self.boton2= Button(self.__ventana, text="Limpiar", padx=55, pady=5, background="#21A118", foreground="white", command=self.Limpiar)
        #----------------------------------------------------------------------------------------
        self.frame= ttk.Frame(self.__ventana, width=345, height=70)
        self.labelFondo= ttk.Label(self.frame, padding=(345,70), background="#56C45C")
        self.labelTexto= ttk.Label(self.frame, text="Tu indice de Masa Corporal (IMC) es", font=Texto, padding=(5,5), background="#56C45C")
        self.labelIMC= ttk.Label(self.frame, textvariable= self.__IMC, font=TextoenNegrita, padding=(5,5), background="#56C45C")
        self.labelPesoFinal= ttk.Label(self.frame, textvariable= self.__pesokgFinal, font=Texto, background="#56C45C", padding=(5,5))
        self.labelKGM2= ttk.Label(self.frame, text="Kg/m2", font=TextoenNegrita, background="#56C45C", padding=(2,5))

        #---Posicionamiento del "menú" usando place---
        self.mensajePrincipal.place(x=230, y=10)
        self.separador1.place(x=50, y=50, bordermode=OUTSIDE, height=0, width=560)
        self.separador2.place(x=50, y=125, bordermode=OUTSIDE, height=0, width=560)
        self.separador3.place(x=50, y=195, bordermode=OUTSIDE, height=0, width=560)
        self.labelEstatura.place(x=70, y=70)
        self.EntryEst.place(x=140, y=75)
        self.EntryKG.place(x=140, y=145)
        self.labelKG.place(x=535, y=144)
        self.labelCM.place(x=535, y=74)
        self.labelPeso.place(x=70, y=140)
        self.boton1.place(x=125, y=205)
        self.boton2.place(x=360, y=205)
        self.__ventana.mainloop()

    def Calcular(self): #Para calcular
        try:
            valor1=float(self.EntryEst.get())
            valor1=valor1/100
            try:
                valor2= float(self.EntryKG.get())
                resultado= valor2/(valor1*valor1)
                resultado=round(resultado,2) #Retorna el resultado con solo 2 decimales
                self.__IMC.set(resultado)

                if self.__IMC.get() < 18.5:
                    self.__pesokgFinal.set("Peso inferior al normal")
                elif self.__IMC.get() < 24.9:
                    self.__pesokgFinal.set("Peso normal")
                elif self.__IMC.get() < 29.9:
                    self.__pesokgFinal.set("Peso superior al normal")
                else:
                    self.__pesokgFinal.set("Obesidad")

                #---Posicionamiento del "resultado" usando place---
                self.frame.place(x=150, y=250)
                self.labelFondo.place(x=0, y=0)
                self.labelTexto.place(x=5, y=5)
                self.labelIMC.place(x=248, y=5)
                self.labelKGM2.place(x=290, y=5)
                self.labelPesoFinal.place(x=105, y=35)

            except: #En caso de que ingrese un valor incorrecto en el peso muestra el mensaje
                messagebox.showerror(title="Error Peso", message="Error en el peso, ingrese un valor correcto.")
                self.__pesokg.set("")
                self.EntryKG.focus()
        except: #En caso de que ingrese un valor incorrecto en la estatura muestra el mensaje
            messagebox.showerror(title="Error Estatura", message= "Error en la estatura, ingrese un valor correcto.")
            self.__estatura.set("")
            self.__pesokg.set("")
            self.EntryEst.focus()

    def Limpiar(self): #Para limpiar el resultado y lo demás
        self.__pesokg.set("")
        self.__estatura.set("")
        self.frame.place(x=1000, y=0)
        self.EntryEst.focus()


