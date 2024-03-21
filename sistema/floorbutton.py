
class FloorButton:
    """Constructor method to initialize an object of the FloorButton class.
            floor_number: The floor number to which the button is associated"""
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.switched_on = False
