from VistaProvincia import ProvinciasView, NewProvincia


#Controlador 1

class ControladorProvincia(object): #Clase que deriva de object
    def __init__(self, repo, vista):
        self.repo= repo #Repositorio
        self.vista= vista #Vista
        self.seleccion= -1 #Selección -1 para que no haya ninguno seleccionado en el listbox
        self.provincias= list(repo.obtenerListaProvincias()) #Obtiene la lista de los pacientes a partir del repositorio (el q tiene el acceso a json)
#comandos que se ejecutan a través de la vista
    def crearProvincia(self):
        nuevaProvincia= NewProvincia(self.vista).show() #Invocación a newprovincia
        if nuevaProvincia: #Si obtuvo una provincia nueva
            provincia = self.repo.agregarProvincia(nuevaProvincia) #Lo agrega
            self.provincias.append(provincia) #Lo agrega a la lista
            self.vista.agregarProvincia(provincia) #Lo muestra

    def seleccionarProvincia(self, index): #Obtiene el indice
        self.seleccion= index
        provincia= self.provincias[index] #Provincia que hay en el indice indicado
        self.vista.verProvinciaEnForm(provincia) #Lo muestra en el formulario de la derecha

    def start(self): #Ejecuta la vista, (la ventana)
        for p in self.provincias:
            self.vista.agregarProvincia(p)
        self.vista.mainloop()

    def salirGrabarDatos(self): #Método de grabar datos para que cuando salga siempre se graben los datos
        self.repo.grabarDatos()
