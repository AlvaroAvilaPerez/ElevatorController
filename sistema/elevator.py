import time


class Elevator:

    def __init__(self, floor_buttons: list):
        """This Constructor Method initializes with specific values for the attributes
                 floor_buttons, floor, current_floor and open
            a -- Floor_buttons: is a parameter passed to the constructor to initialize the attribute"""
        self.floor_buttons = floor_buttons
        self.floor = 0
        self.current_floor = 0
        self.open = False

    def go_to_floor(self, floor_number: int):
        """This method makes the elevator go to the defined floor"
                 a -- floor_number: which represents the number of the floor to which you want to go """
        buttons = list(filter(lambda button: button.floor_number == floor_number, self.floor_buttons))
        print('----------------')
        button_pressed = buttons[0]
        print(f'--Going to the Floor: {button_pressed.floor_number}')
        print(f'Current Floor: {self.current_floor}')
        while self.current_floor != floor_number:
            if self.current_floor < floor_number:
                self.gou_up_floor()
            else:
                self.go_down_floor()
            print("Floor : " + str(self.current_floor))
            print('----------------')
        else:
            print(f'Go floor!!{floor_number} ')
            self.open_elevator()
            print('----------------')

        if floor_number > len(self.floor_buttons):
            print(f'Error!!! This floor  {floor_number} It does not exist in the tower building.')
            return

    def gou_up_floor(self):
        """ This this function updates the value of the current_floor and adds 1 to the value """
        self.current_floor = self.current_floor + 1

    def go_down_floor(self):
        """ This function updates the value of the current floor and subtracts 1 from the value. """
        self.current_floor = self.current_floor - 1

    def open_elevator(self):
        """This Method controls whether the elevator is open or closed."""

        print("<<<<<< OPEN ELEVATOR >>>>>>")
        time.sleep(2)
        print("<<<<<< CLOSED ELEVATOR  >>>>>>")