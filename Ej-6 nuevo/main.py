from RepositorioProvincia import RepositorioProvincia
from Controlador import ControladorProvincia
from VistaProvincia import ProvinciasView
from Decodificador import Decodificador

 #En los comentarios sería paciente=provincia
def main():
    conn= Decodificador("datos.json")#Obtenemos los datos del JSON
    repo= RepositorioProvincia(conn)#Obtiene el objeto repositorio
    vista= ProvinciasView()#Vista de los pacientes
    ctrl= ControladorProvincia(repo, vista)#Controlador con repositorio y la vista
    vista.setControlador(ctrl)#A la vista le establece el controlador (Vista 4)
    ctrl.start() #Inicia el controlador, ejecuta para cada uno de los pacientes, los agrega y los muestra con mainloop y se queda esperando a q hagamos algo
    ctrl.salirGrabarDatos()#Antes de salir graba datos

if __name__== "__main__":
    main()
