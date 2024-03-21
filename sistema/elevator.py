import time
class Elevator:
    """
     Initializes a new instance of the Elevator class.
        :parameter floor_buttons: is a list of buttons for each floor, indicating whether the button is pressed or not.
        : self.floor = 0, current elevator floor
        : self.current_floor = 0, The floor the elevator is currently on
        : self.open = False, Indicates whether the elevator doors are open or closed
     """
    def __init__(self, floor_buttons: list):
        self.floor_buttons = floor_buttons
        self.floor = 0
        self.current_floor = 0
        self.open = False

    """
     Move the elevator to the specified floor.
     :floor_number: The number of the floor you want to go to.
     """
    def go_to_floor(self, floor_number: int):
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

    """ This function updates the current_floor value by incrementing it by 1.
                 Increments the value of current_floor by 1 to indicate that the elevator is moving up
                 in the building."""
    def go_up_floor(self):
        self.current_floor = self.current_floor + 1
        print(self.current_floor)

    """ This function updates the current_floor value by decrementing it by 1.
                 Decrements the value of current_floor by 1 to indicate that the elevator is moving down
                 in the building"""
    def lower_floor(self):
        self.current_floor = self.current_floor - 1

    """This method simulates the process of opening and closing elevator doors.
             First the status of the doors is set to open, wait a while and then close"""
    def open_elevator(self):
        print("<<<<<< OPEN ELEVATOR >>>>>>")
        time.sleep(2)
        print("<<<<<< CLOSE ELEVATOR >>>>>>")
