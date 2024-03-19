
class FloorButton:
    """Metodo constructor que guarda el numero de piso y encendido donde indica si el boton esta encendido o apagado"""
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.switched_on = False
