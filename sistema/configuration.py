from sistema.floor import Floor
from sistema.elevator import Elevator
from sistema.floorButton import FloorButton
from sistema.tower import Tower


class Setting:
    """This class is used to create and configure elevators and floors, and
         to find the closest elevator to a specific floor within the settings"""
    def __init__(self, floor_number, number_of_elevators):
        """This builder method creates elevators where each elevator has its floor buttons"""
        self.floor_number = floor_number
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        for _ in range(number_of_elevators + 1):
            floor_buttons = [FloorButton(i) for i in range(floor_number + 1)]
            elevator = Elevator(floor_buttons)
            self.elevators.append(elevator)
        self.floors = [Floor(i, self.elevators[0]) for i in range(floor_number + 1)]
        for i, elevator in enumerate(self.elevators):
            print(f'Elevator {i}')

    def get_elevator_plus_nearby(self, floor_number: str):
        """This method manages an elevator system the purpose of this method is to find
             the closest elevator to a certain floor number
            a -- floor_number  This is the floor number for which we want to find the nearest elevator."""
        elevator_plus_nearby = None
        floor_difference_real = len(self.elevators[0].floor_buttons)
        for elevator in self.elevators:
            floor_difference = abs(elevator.current_floor - floor_number)
            if floor_difference < floor_difference_real:
                floor_difference_real = floor_difference
                elevator_plus_nearby = elevator

        if elevator_plus_nearby:
            print(
                f"The elevator closest to the floor {floor_number} It's the elevator on the floor {elevator_plus_nearby.current_floor}.")

        print(elevator_plus_nearby.current_floor)
        return elevator_plus_nearby