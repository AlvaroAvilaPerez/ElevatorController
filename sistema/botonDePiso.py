
class BotonDePiso:
    """ Es una funcion donde numero de piso guarda el numero de piso y encendido que indica si el botón está encendido
        o apagado por defecto esta apgado"""
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False