from sistema.configuracionEdificio import Configuracion


class Edificio:

    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores

edificio_torre = Configuracion(20, 3)
edificio_torre.pisos[0].llamar_ascensor(arriba=True)
edificio_torre.ascensores[0].ir_al_piso(15)
edificio_torre.ascensores[2].ir_al_piso(2)
edificio_torre.ascensores[3].ir_al_piso(1)
ascensor_cercano = edificio_torre.get_ascensor_mas_cercano(5)
