class Building:
    def __init__(self, floors, elevators):
        """ This constructor defines a class called Building that represents a building.
            It has a special method __init__, which is the constructor of the class.

            Keyword arguments:
            floors (int) -- The number of floors in the elevator system.
            elevators (int) -- The number of elevators in the system.
        """
        self.floors = floors
        self.elevators = elevators
