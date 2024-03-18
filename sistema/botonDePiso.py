

class BotonDePiso:
    def __init__(self, numero_de_piso):
        """ Este  metodo constructor hace que guarde el numero de piso y encendido que indica si el botón está encendido
                    o apagado por defecto esta apgado"""
        self.numero_de_piso = numero_de_piso
        self.encendido = False