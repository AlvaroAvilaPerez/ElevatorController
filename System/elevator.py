import time


class Elevator:
    def __init__(self, floor_buttons: list):
        """ The constructor initializes an instance of the Elevator class with the specified list of floor buttons.
            Sets the current floor and the floor the elevator is on to 0 by default.
            Set the door status to closed by default.

            Keyword arguments:
            floor_buttons (list) -- A list of floor buttons available in the elevator
            Assigns a list of floor buttons
            current_floor (int) -- current floor as 0
            the door closed and the current floor as 0
        """
        self.floor_buttons = floor_buttons
        self.floor = 0
        self.current_floor = 0
        self.open = False

    def go_to_floor(self, floor_number: int):
        """ This method verify if the specified floor exists in the elevator button list.
            If the floor does not exist, print an error message.
            If the floor exists, move the elevator to that floor, printing the details of the move

            Keyword arguments:
            floor_number (int) -- The floor number to which you want to move the elevator
            This method checks if the specified floor exists in the elevator button list
            If the floor does not exist, print an error message
            If the floor exists, move the elevator to that floor
        """
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

    def go_up_floor(self):
        """ This function updates the current_floor value by incrementing it by 1
            Increments the value of current_floor by 1 to indicate that the elevator is moving up
            in the building.
        """
        self.current_floor = self.current_floor + 1
        print(self.current_floor)

    def lower_floor(self):
        """ This function updates the current_floor value by decrementing it by 1.
            Decrements the value of current_floor by 1 to indicate that the elevator is moving down
            in the building.
        """
        self.current_floor = self.current_floor - 1

    def open_elevator(self):
        """ This method simulates the process of opening and closing elevator doors
            First the status of the doors is set to open, wait a while and then close.
        """
        print("<<<<<< OPEN ELEVATOR >>>>>>")
        time.sleep(2)
        print("<<<<<< CLOSE ELEVATOR >>>>>>")