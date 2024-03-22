from sistema.floors import Floor
from sistema.elevator import Elevator
from sistema.floorbutton import FloorButton


class Setting:
    def __init__(self, floor_numbers: int, number_of_elevators: list):
        """ This method initializes a configuration that includes the creation of elevator and floor objects,
            assigning floor buttons to each elevator

            Keyword arguments:
            floor_number -- The total number of floors in the building.
            number_of_elevators -- A list containing the total number of elevators to create.
        """
        self.floor_number = floor_numbers
        self.number_of_elevators = number_of_elevators
        self.elevators = [Elevator([FloorButton(i) for i in range(floor_numbers + 1)]) for _ in
                          range(number_of_elevators + 1)]
        self.floors = [Floor(i, self.elevators[0]) for i in range(floor_numbers + 1)]
        for i, elevator in enumerate(self.elevators):
            print(f'Ascensor {i}')

    def get_closest_elevator(self, floor_number: int):
        """ This method, get_closest_elevator, has the function of finding the elevator closest to the floor you want

             Keyword arguments:
             floor_number -- Indicates the number of the desired floor to which you want to find the closest elevator.
             return nearest_elevator find the elevator
        """
        nearest_elevator = None
        difference_of_real_floors = len(self.elevators[0].floor_buttons)
        for elevator in self.elevators:
            floor_difference = abs(elevator.current_floor - floor_number)
            if floor_difference < difference_of_real_floors:
                difference_of_real_floors = floor_difference
                nearest_elevator = elevator

        if nearest_elevator:
            print(
                f"The elevator closest to the floor {floor_number} is the elevator on the floor {nearest_elevator.current_floor}.")
        return nearest_elevator
