
class Floor:
    def __init__(self, floor_number: int, elevator):
        """ The constructor initializes an instance of the Floor class with the floor number and the associated
            elevator object, sets variables to indicate whether the up and down buttons
            are activated (False by default) and the elevator opening time on this floor (5 seconds by default).

            Keyword arguments:
            floor_number (int) -- The floor number.
            elevator -- The instance of an elevator object associated with this floor.
        """
        self.floor_number = floor_number
        self.above_button = False
        self.down_button = False
        self.elevator = elevator
        self.elevator_opening_time = 5

    def call_elevator(self, above: str):
        """ This method is responsible for simulating the process of calling an elevator from a specific floor

            Keyword arguments:
            above -- evaluates to true for example if a non-empty string is provided
        """
        if above:
            self.above_button = True
            self.above_button = False
        else:
            print("Going down:.........")
            self.down_button = True
            self.down_button = False