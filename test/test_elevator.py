
from sistema.elevator import Elevator
from sistema.floorButton import FloorButton


def test_gou_up_floor():
    floor_buttons = FloorButton(0)
    elevator_t = Elevator([floor_buttons])
    elevator_t.gou_up_floor()
    assert elevator_t.current_floor == 1


def test_go_down_floor():
    floor_buttons = FloorButton(3)
    elevator_t = Elevator([floor_buttons])
    elevator_t.current_floor = 15
    elevator_t.gou_up_floor()
    assert elevator_t.current_floor == 14


def test_go_to_the_floor_not_exist():
    floor_n = Elevator([FloorButton(i) for i in range(5)])
    result = floor_n.go_to_floor(10)
    assert result is False

    result = floor_n.go_to_floor(4)
    assert result is True


def test_go_to_floor():
    elevator = Elevator([FloorButton(i) for i in range(10)])
    elevator.go_to_floor(8)
    assert elevator.current_floor == 8