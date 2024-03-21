from floors import Floor
from elevator import Elevator
from floorbutton import FloorButton

class Setting():
    """ This method lists and creates the specified number of elevators.
             :floor_number: The total number of floors in the building
             :number_of_elevators: The total number of elevators to be created.
             """
    def __init__(self, floor_number: int, number_of_elevators: list):
        self.floor_number = floor_number
        self.number_of_elevators = number_of_elevators
        self.elevators = [Elevator([FloorButton(i) for i in range(floor_number + 1)]) for _ in range(number_of_elevators + 1)]
        self.floors = [Floor(i, self.elevators[0]) for i in range(floor_number + 1)]
        for i, elevator in enumerate(self.elevators):
            print(f'Ascensor {i}')

    """ Find the elevator closest to the desired floor.
             This method loops through all the elevators in the list and determines which one is closest to the desired floor.
             floor_number: The number of the desired floor.
             :The elevator object closest to the desired floor, or None if no elevators are available.
         """
    def get_closest_elevator(self, floor_number: int):
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
