class Building:
    def __init__(self, floors, elevators):
        """ The constructor initializes an instance of the class representing an elevator system.

            Keyword arguments::
            floors (int) -- The number of floors in the elevator system.
            elevators (int) -- The number of elevators in the system.
        """
        self.floors = floors
        self.elevators = elevators
