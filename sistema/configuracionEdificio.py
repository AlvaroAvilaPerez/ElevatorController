from sistema.pisos import Piso, BotonDePiso
from sistema.ascensor import Ascensor

class Configuracion():
    def __init__(self, numero_de_piso, numero_de_ascensores):
        self.numero_de_piso = numero_de_piso
        self.numero_de_ascensores = numero_de_ascensores
        self.ascensores = list(filter(lambda ascensor: ascensor.BotonDePiso == BotonDePiso, self.numero_de_ascensores))
        self.botones_de_pisos_A = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.pisos = [Piso(i, self.ascensores[0]) for i in range(numero_de_piso + 1)]
        # enumera y nos lista la cantidad e ascensores
        for i, ascensor in enumerate(self.ascensores):
            print(f'Ascensor {i}')
