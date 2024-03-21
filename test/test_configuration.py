from sistema.elevator import Elevator
from sistema.configuration import Setting
from sistema.floorButton import FloorButton


def test_get_elevator_plus_nearby():
    floor_number = 10
    number_of_elevators = 3
    elevator_s = Setting(floor_number, number_of_elevators)
    elevator_s.elevators = [Elevator([FloorButton(i) for i in range(floor_number + 1)]) for _ in range(number_of_elevators + 1)]
    elevator_s.elevators[0].current_floor = 4
    elevator_s.elevators[1].current_floor = 5
    elevator_s.elevators[2].current_floor = 5
    result = elevator_s.get_elevator_plus_nearby(5)
    assert result.current_floor == 5