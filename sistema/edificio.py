from sistema.configuracionEdificio import Configuracion


class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores


edificio_torre = Configuracion(20, 4)
edificio_torre.pisos[0].llamar_ascensor(arriba=True)
print('------ASCENSOR "A"----------')
edificio_torre.ascensor.ir_al_piso(25)
edificio_torre.ascensor.ir_al_piso(2)

# print('------ASCENSOR "B"----------')
# edificio_torre.ascensorB.ir_al_piso(5)
# edificio_torre.ascensorB.ir_al_piso(1)
# edificio_torre.ascensorB.ir_al_piso(0)
# edificio_torre.ascensorB.ir_al_piso(2)
#
# print('------ASCENSOR "C"----------')
# edificio_torre.ascensorC.ir_al_piso(6)
# edificio_torre.ascensorC.ir_al_piso(3)