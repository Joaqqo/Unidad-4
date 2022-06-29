from tkinter import *
from tkinter import ttk, font, messagebox


class App():
    __ventana=None
    __precio=None
    __iva=None
    __seleccion=None
    __precioIVA=None


    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.geometry("300x350")
        self.__ventana.configure(background='white')
        self.__ventana.resizable(0,0)
        self.__ventana.title("Cálculo de IVA")
        #----------------------------------------------------------------------------------------
        self.__precio=StringVar()
        self.__iva=StringVar()
        self.__seleccion=IntVar()
        self.__precioIVA=StringVar()
        self.mensajePrincipal= ttk.Label(self.__ventana, text="Cálculo de IVA", padding=(5,5))
        #---------Creación de separadores, entrys, labels, etc-----------------------------------
        self.separador1= ttk.Separator(self.__ventana, orient=HORIZONTAL)
        #----------------------------------------------------------------------------------------
        self.labelIVA= ttk.Label(self.__ventana, text="IVA", padding=(5,5),background="white")
        self.labelconIVA= ttk.Label(self.__ventana, text="Precio con IVA", padding=(5,5), background="white")
        self.labelFondo= ttk.Label(self.__ventana,text="Cálculo de IVA", padding=(200,20), background="#4cb6c2")
        self.labelsinIVA= ttk.Label(self.__ventana, text="Precio sin IVA", padding=(5,5),background="white")
        self.labelconIVAres= ttk.Label(self.__ventana, textvariable= self.__precioIVA, padding=(5,5), width=20, background="grey")
        self.labelIVAres= ttk.Label(self.__ventana, textvariable=self.__iva, padding=(5,5), width=20, background="grey")
        #----------------------------------------------------------------------------------------
        self.boton1= Button(self.__ventana, text="Calcular", padx=20, pady=5, background="#21A118", foreground="white", command=self.Calcular)
        self.boton2= Button(self.__ventana, text="Salir", padx=25, pady=5, background="#FF0000", foreground="white", command=self.Salir)
        boton3= ttk.Radiobutton(text="IVA 21%", value=21, variable=self.__seleccion,style="Wild.TRadiobutton")
        boton4= ttk.Radiobutton(text="IVA 10,5%", value=10, variable=self.__seleccion,style="Wild.TRadiobutton")
        #----------------------------------------------------------------------------------------
        self.entryIVA= ttk.Entry(self.__ventana, textvariable= self.__precio, width=20)
        #----------------------------------------------------------------------------------------
        #Places
        self.separador1.place(x=0, y=59, bordermode=OUTSIDE, height=0, width=460)
        self.labelFondo.place(x=-90, y=0)
        self.boton1.place(x=10, y=300)
        self.boton2.place(x=200, y=300)
        boton3.place(x=0,y=130)
        boton4.place(x=0,y=160)
        self.labelIVA.place(x=0, y=200)
        self.labelconIVA.place(x=0, y=240)
        self.labelsinIVA.place(x=0, y=68)
        self.entryIVA.place(x=150, y=70)
        self.labelconIVAres.place(x=150, y=240)
        self.labelIVAres.place(x=150, y=200)
        self.__ventana.mainloop()

    def Calcular(self):
        iva=None
        try:
            Precio= float(self.__precio.get())
        except ValueError:
            messagebox.showerror(title="ERROR", message="Por favor, ingrese un número")
            return
        else:
            if self.__seleccion.get()==10:
                iva=0.105
            elif self.__seleccion.get()==21:
                iva=0.21

            total=Precio+Precio*iva
            totaldos= Precio*iva
            self.__precioIVA.set(total)
            self.__iva.set(totaldos)


    def Salir(self):
        self.__ventana.destroy()


