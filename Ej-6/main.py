from RepositorioProvincia import RepositorioProvincia
from Controlador import ControladorProvincia
from VistaProvincia import ProvinciasView
from Decodificador import Decodificador


def main():
    conn= Decodificador("datos.json")
    repo= RepositorioProvincia(conn)
    vista= ProvinciasView()
    ctrl= ControladorProvincia(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__== "__main__":
    main()
