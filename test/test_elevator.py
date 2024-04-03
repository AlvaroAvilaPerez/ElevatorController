from System.elevator import Elevator
from System.floorbutton import FloorButton


def test_go_up_floor():
    floor_button = FloorButton(0)
    elevator_t = Elevator([floor_button])
    elevator_t.go_up_floor()
    assert elevator_t.current_floor == 1


def test_lower_floor():
    floor_button = FloorButton(3)
    elevator_t = Elevator([floor_button])
    elevator_t.current_floor = 15
    elevator_t.lower_floor()
    assert elevator_t.current_floor == 14


def test_go_to_floor():
    elevator = Elevator([FloorButton(i) for i in range(10)])
    elevator.go_to_floor(8)
    assert elevator.current_floor == 8