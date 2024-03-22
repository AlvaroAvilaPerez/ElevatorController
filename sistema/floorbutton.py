class FloorButton:
    def __init__(self, floor_number: int):
        """ The constructor initializes an instance of the FloorButton class with the specified floor number.
            Set the button state to off by default

            Keyword arguments:
            floor_number (int) -- The floor number associated with the button
        """
        self.floor_number = floor_number
        self.switched_on = False
