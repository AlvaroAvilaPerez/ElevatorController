import time


class Piso:
    def __init__(self, numero_piso, ascensor):
        self.numero_piso = numero_piso
        self.boton_arriba = False
        self.boton_abajo = False
        self.ascensor = ascensor
        self.tiempo_de_apertura_ascensor = 5

    def llamar_ascensor(self, arriba):
        """ En esta funcion hace que si el ascensor que va arriba significa true,
                      y si el usuario quiere bajar es false """
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
        """ Este Metodo control si el ascensor está abierto o cerrado."""

        print("<<<<<< ABRIR ASCENSOR >>>>>>")
        self.ascensor.abrir = True
        time.sleep(2)
        self.ascensor.abrir = False
        print("<<<<<< CERRAR ASCENSOR  >>>>>>")
