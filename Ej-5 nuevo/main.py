from RepositorioContactos import RespositorioContactos
from VistaPaciente import PatientsView
from Controlador import ControladorPacientes
from Decodificador import ObjectEncoder

def main():
    conn= ObjectEncoder("pacientes.json") #Obtenemos los datos del JSON
    repo= RespositorioContactos(conn) #Obtiene el objeto repositorio
    vista= PatientsView() #Vista de los pacientes
    ctrl= ControladorPacientes(repo, vista) #Controlador con repositorio y la vista
    vista.setControlador(ctrl) #A la vista le establece el controlador (Vista 4)
    ctrl.start() #Inicia el controlador, ejecuta para cada uno de los pacientes, los agrega y los muestra con mainloop y se queda esperando a q hagamos algo
    ctrl.salirGrabarDatos() #Antes de salir graba datos

if __name__ == "__main__":
    main()
