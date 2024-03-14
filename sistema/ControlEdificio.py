from sistema.Pisos import Piso, BotonDePiso
from sistema.Ascensor import Ascensor

class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores
class Configuracion():
    def __init__(self, numero_de_piso, ascensor):
        self.numero_de_piso = numero_de_piso
        self.ascensor = ascensor
        self.botones_de_pisos_A = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.botones_de_pisos_B = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.botones_de_pisos_C = [BotonDePiso(i) for i in range(self.numero_de_piso + 1)]
        self.ascensorA = Ascensor(self.botones_de_pisos_A)
        self.ascensorB = Ascensor(self.botones_de_pisos_B)
        self.ascensorC = Ascensor(self.botones_de_pisos_C)
        self.pisos = [Piso(i, self.ascensorA) for i in range(self.numero_de_piso + 1)]


edificio_torre = Configuracion(20, 3)
edificio_torre.pisos[0].llamar_ascensor(arriba=True)
print('------ASCENSOR "A"----------')
edificio_torre.ascensorA.ir_al_piso(25)
edificio_torre.ascensorA.ir_al_piso(2)

print('------ASCENSOR "B"----------')
edificio_torre.ascensorB.ir_al_piso(5)
edificio_torre.ascensorB.ir_al_piso(1)
edificio_torre.ascensorB.ir_al_piso(0)
edificio_torre.ascensorB.ir_al_piso(2)

print('------ASCENSOR "C"----------')
edificio_torre.ascensorC.ir_al_piso(6)
edificio_torre.ascensorC.ir_al_piso(3)
