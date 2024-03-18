
class Ascensor:

    def __init__(self, botones_de_piso):
        """Este Metodo Constructor inicializa con valores especificos para lo atributos
                botones_de_piso, piso, piso_actual y abierto
           a -- Botones_de_piso: es un parámetro que se pasa al constructor para inicializar el atributo"""
        self.botones_de_piso = botones_de_piso
        self.piso = 0
        self.piso_actual = 0
        self.abierto = False

    def ir_al_piso(self, numero_de_piso):
        """ Este metodo hace que el ascensor vaya al piso definido """

        if numero_de_piso > len(self.botones_de_piso):
            print(f'Error!!! Este piso  {numero_de_piso} no existe en el edificio torre.')
            return
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
            print("Piso : " + str(self.piso_actual))
            print('----------------')
        else:
            print(f'LLegaste al piso !!{numero_de_piso} ')
            print('----------------')

    def subir_piso(self):
        """ Esta esta funcion  actualiza el valor del piso_actual y Resta 1 al valor """
        self.piso_actual = self.piso_actual + 1

    def bajar_piso(self):
        """ Esta esta funcion  actualiza el valor del piso_actual y Resta 1 al valor """
        self.piso_actual = self.piso_actual - 1
