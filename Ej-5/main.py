from RepositorioContactos import RespositorioContactos
from VistaPaciente import PatientsView
from Controlador import ControladorPacientes
from Decodificador import ObjectEncoder

def main():
    conn= ObjectEncoder("pacientes.json")
    repo= RespositorioContactos(conn)
    vista= PatientsView()
    ctrl= ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
