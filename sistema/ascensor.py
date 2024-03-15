from datetime import time


class Ascensor:
    def __init__(self, botones_de_piso):
        self.botones_de_piso = botones_de_piso
        self.piso = 0
        self.piso_actual = 0
        self.abierto = False

        """ Comprueba si el número del piso al que se desea ir es válido,
           verifica si Numero de piso es mayor que los botones de piso"""

    def ir_al_piso(self, numero_de_piso):
        if numero_de_piso > len(self.botones_de_piso) - 1:
            print(f'Error!!! Este piso  {numero_de_piso} no existe en el edificio torre.')
            return

        botones = list(filter(lambda button: button.numero_de_piso == numero_de_piso, self.botones_de_piso))
        print('----------------')
        boton_presionado = botones[0]
        print(f'--Yendo al Piso: {boton_presionado.numero_de_piso}')
        print(f'Piso Actual: {self.piso_actual}')

        """ Es bucle se ejecuta mientras el piso actual no sea igual al piso,
                   al que se desea ir dentro de el ejecuta si debe ir arriba o abajo"""
        while self.piso_actual != numero_de_piso:
            if self.piso_actual < numero_de_piso:
                self.subir_piso()
            else:
                self.bajar_piso()
            print("Piso : " + str(self.piso_actual))

            print('----------------')
        else:
            print(f'LLegaste al piso !!{numero_de_piso} ')
            print('----------------')

    """ Esta esta funcion  actualiza el valor del piso_actual y Resta 1 al valor """
    def subir_piso(self):
        self.piso_actual = self.piso_actual + 1

    """ Esta esta funcion  actualiza el valor del piso_actual y Resta 1 al valor """
    def bajar_piso(self):
        self.piso_actual = self.piso_actual - 1