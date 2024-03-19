import time

class Floor:
    def __init__(self, floor_number, elevator):
        self.floor_number = floor_number
        self.above_button = False
        self.boton_abajo = False
        self.elevator = elevator
        self.elevator_opening_time = 5

    """ En esta funcion hace que si el ascensor va arriba significa true,
        y si el usuario quiere bajar es false """
    def call_elevator(self, above):
        if above:
            self.above_button = True
            self.above_button = False
        else:
            print("Going down:.........")
            self.down_button = True
            self.down_button = False
