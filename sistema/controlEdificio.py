import time


class Edificio:
    def __init__(self, pisos, ascensores):
        self.pisos = pisos
        self.ascensores = ascensores


class Piso:
    def __init__(self, numero_piso, ascensor):
        self.numero_piso = numero_piso
        self.boton_arriba = False
        self.boton_abajo = False
        self.ascensor = ascensor
        self.tiempo_de_apertura_ascensor = 5


    def llamar_ascensor(self, arriba):
        if arriba:
            print("Subiendo:^^^^^^^")
            self.boton_arriba = True
            self.abrir_ascensor()
            self.boton_arriba = False
        else:
            print("Bajando:.........")
            self.boton_abajo = True
            self.abrir_ascensor()
            self.boton_abajo = False

    def abrir_ascensor(self):
        print("Se Abre el Ascensor")
        self.ascensor.abierto = True
        time.sleep(self.tiempo_de_apertura_ascensor)
        self.ascensor.abierto = False
        print("Se Cierra el Ascensor")


class Ascensor:
    def __init__(self, botones_de_piso):
        self.botones_de_piso = botones_de_piso
        self.piso_actual = 0
        self.abierto = False


    def ir_al_piso(self, numero_de_piso):
        botones = list(filter(lambda button: button.numero_de_piso == numero_de_piso, self.botones_de_piso))
        print('----------------')
        boton_presionado = botones[0]
        print(f'--Yendo al Piso: {boton_presionado.numero_de_piso}')
        print(f'Piso Actual: {self.piso_actual}')
        while self.piso_actual != numero_de_piso:
            if self.piso_actual < numero_de_piso:
                self.subir_piso()
            else:
                self.bajar_piso()
            print("Piso: " + str(self.piso_actual))
        print('----------------')

    def subir_piso(self):
        self.piso_actual = self.piso_actual + 1

    def bajar_piso(self):
        self.piso_actual = self.piso_actual - 1

class BotonDePiso:
            def __init__(self, numero_de_piso):
                self.numero_de_piso = numero_de_piso
                self.encendido = False

class Configuracion():
    def __init__(self):
        self.piso = 0
        self.ascensor = None
        self.botones_de_piso = set()


    def edificio_torre(self):
        while True:
        edificio.ascensor = Ascensor()
        edificio.ascensor.piso = ascensor_piso
        edificio.botones_de_piso = set(botones_de_pisos)
        if piso.llamar_ascensor():
        ascensorA.ir_al_piso(piso.numero_piso)

        return edificio


edificio_torre = Configuracion(3, 1)
edificio_torre = Configuracion(4, 1)
edificio_torre = Configuracion(7, 1)