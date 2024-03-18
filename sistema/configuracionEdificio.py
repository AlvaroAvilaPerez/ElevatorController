from sistema.pisos import Piso
from sistema.ascensor import Ascensor
from sistema.botonDePiso import BotonDePiso


class Configuracion():
    def __init__(self, numero_de_piso, numero_de_ascensores):
        self.numero_de_piso = numero_de_piso
        self.numero_de_ascensores = numero_de_ascensores
        self.ascensores = [Ascensor([BotonDePiso(i) for i in range(numero_de_piso + 1)]) for _ in range(numero_de_ascensores + 1)]
        self.pisos = [Piso(i, self.ascensores[0]) for i in range(numero_de_piso + 1)]
        for i, ascensor in enumerate(self.ascensores):
            print(f'Ascensor {i}')

    def get_ascensor_mas_cercano(self, numero_piso):
        ascensor_mas_cercano = None
        diferencia_de_pisos_real = len(self.ascensores[0].botones_de_piso)
        for ascensor in self.ascensores:
            diferencia_de_pisos = abs(ascensor.piso_actual - numero_piso)
            if diferencia_de_pisos < diferencia_de_pisos_real:
                diferencia_de_pisos_real = diferencia_de_pisos
                ascensor_mas_cercano = ascensor

        if ascensor_mas_cercano:
            print(
                f"El ascensor más cercano al piso {numero_piso} es el ascensor en el piso {ascensor_mas_cercano.piso_actual}.")
        return ascensor_mas_cercano
