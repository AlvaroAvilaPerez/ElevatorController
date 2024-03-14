import time

class Piso:
    def __init__(self, numero_piso, ascensor):
        self.numero_piso = numero_piso
        self.boton_arriba = False
        self.boton_abajo = False
        self.ascensor = ascensor
        self.tiempo_de_apertura_ascensor = 5

    def llamar_ascensor(self, arriba):
        if arriba:
            self.boton_arriba = True
            self.abrir_ascensor()
            self.boton_arriba = False
        else:
            print("Bajando:.........")
            self.boton_abajo = True
            self.abrir_ascensor()
            self.boton_abajo = False

    def abrir_ascensor(self):
        print("<<<<<< ABRIR ASCENSOR >>>>>>")
        self.ascensor.abierto = True
        time.sleep(2)
        self.ascensor.abierto = False
        print("<<<<<< CERRAR ASCENSOR  >>>>>>")

class BotonDePiso:
    def __init__(self, numero_de_piso):
        self.numero_de_piso = numero_de_piso
        self.encendido = False