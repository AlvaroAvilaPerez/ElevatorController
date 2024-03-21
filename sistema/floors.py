import time

class Floor:
    def __init__(self, floor_number: int, elevator):
        self.floor_number = floor_number
        self.above_button = False
        self.boton_abajo = False
        self.elevator = elevator
        self.elevator_opening_time = 5

    """ In this function it means that if the elevator goes up it means true,
             and if the user wants to down it is false """
    def call_elevator(self, above: str):
        if above:
            self.above_button = True
            self.above_button = False
        else:
            print("Going down:.........")
            self.down_button = True
            self.down_button = False
