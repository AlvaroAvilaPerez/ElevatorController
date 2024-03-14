from sistema.pisos import Piso, BotonDePiso
from sistema.ascensor import Ascensor

class Configuracion():
    def __init__(self, numero_de_piso, ascensor):
        self.numero_de_piso = numero_de_piso
        self.ascensor = ascensor
        self.botones_de_pisos = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.pisos = [Piso(i, self.ascensor) for i in range(self.numero_de_piso + 1)]
        for i in range(ascensor):
            # self.botones_de_pisos = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
            print(i)
