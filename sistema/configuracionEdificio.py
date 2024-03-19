from pisos import Floor
from ascensor import Elevator
from botonDePiso import FloorButton


class Setting():
    """enumera y nos lista la cantidad e ascensores
              el +1 hace que me cuete des el numero 1 de ascensores y no el 0"""
    def __init__(self, floor_number, number_of_elevators):
        self.floor_number = floor_number
        self.number_of_elevators = number_of_elevators
        self.elevators = [Elevator([FloorButton(i) for i in range(floor_number + 1)]) for _ in range(number_of_elevators + 1)]
        self.floors = [Floor(i, self.elevators[0]) for i in range(floor_number + 1)]
        for i, elevator in enumerate(self.elevators):
            print(f'Ascensor {i}')

    """Este método recorre todos los ascensores en la lista y determina cuál está más cerca del piso deseado"""
    def get_closest_elevator(self, floor_number):
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
