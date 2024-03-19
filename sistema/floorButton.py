

class FloorButton:
    def __init__(self, floor_number):
        """ This constructor method makes it save the floor and power number that indicates if the button is on
                      or off by default it is off"""
        self.floor_number = floor_number
        self.powerOn = False