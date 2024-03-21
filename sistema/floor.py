
class Floor:
    def __init__(self, floor_number, elevator):
        self.floor_number = floor_number
        self.up_button = False
        self.down_button = False
        self.elevator = elevator
        self.elevator_opening_time = 5

    def call_elevator(self, up):
        """ In this function it means that if the elevator going up means true,
                       and if the user wants to download it is false """
        if up:
            self.up_button = True

            self.up_button = False
        else:
            print("Going down:.........")
            self.down_button = True
            self.down_button = False