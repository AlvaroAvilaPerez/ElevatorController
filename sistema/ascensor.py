import time
class Elevator:
    """
       Inicializa una nueva instancia de la clase Elevador.

       :parametro floor_buttons: es una lista de botones para cada piso, indicando si el botón está presionado o no.
       : self.floor = 0, piso actual del elevador
       : self.current_floor = 0, El piso en el que se encuentra actualmente el elevador
       : self.open = False, Indica si las puertas del elevador están abiertas o cerradas
       """
    def __init__(self, floor_buttons):
        self.floor_buttons = floor_buttons
        self.floor = 0
        self.current_floor = 0
        self.open = False

    """
    Mueve el ascensor al piso especificado.
    :floor_number: El número del piso al que se desea ir.
    """
    def go_to_floor(self, floor_number):
        if floor_number > len(self.floor_buttons):
            print(f'Mistake!!! This floor  {floor_number} It does not exist in the tower building.')
            return
        buttons = list(filter(lambda button: button.floor_number == floor_number, self.floor_buttons))
        print('----------------')
        button_pressed = buttons[0]
        print(f'--Going to the Floor: {button_pressed.floor_number}')
        print(f'Current Floor: {self.current_floor}')
        while self.current_floor != floor_number:
            if self.current_floor < floor_number:
                self.go_up_floor()
            else:
                self.lower_floor()
            print("floor : " + str(self.current_floor))
            print('----------------')
        else:
            print(f'Reached the floor !!{floor_number} ')
            self.open_elevator()
            print('----------------')

    """Esta esta funcion  actualiza el valor del piso_actual y suma 1 al valor"""
    def go_up_floor(self):
        self.current_floor = self.current_floor + 1
        print(self.current_floor)

    """Esta esta funcion  actualiza el valor del piso_actual y Resta 1 al valor"""
    def lower_floor(self):
        self.current_floor = self.current_floor - 1

    """este método simula el proceso de abrir y cerrarlas puertas del ascensor.
        Primero se establece el estado de las puertas como abiertas, espera un tiempo y luego se cierra"""
    def open_elevator(self):
        print("<<<<<< OPEN ELEVATOR >>>>>>")
        time.sleep(2)
        print("<<<<<< CLOSE ELEVATOR >>>>>>")
