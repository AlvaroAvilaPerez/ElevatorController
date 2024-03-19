from sistema.elevator import Elevator
from sistema.floorButton import FloorButton


def test_gou_up_floor():
    floor_buttons = FloorButton(0)
    elevator_t = Elevator([floor_buttons])
    result = elevator_t.gou_up_floor()
    assert elevator_t.current_floor == 1


# def test_go_to_floor():
#     elevator = Elevator()
#     elevator.current_floor = 0
#     elevator.floor_buttons = []
#
#     result = elevator.go_to_floor(5)
#     assert elevator.current_floor == 5
#
#     elevator.go_to_floor(10)
#     assert elevator.current_floor == 10
