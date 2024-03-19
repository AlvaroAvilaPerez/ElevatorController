
from sistema.elevator import Elevator
from sistema.floorButton import FloorButton


def test_gou_up_floor():
    floor_buttons = FloorButton(0)
    elevator_t = Elevator([floor_buttons])
    result = elevator_t.gou_up_floor()
    assert elevator_t.current_floor == 1


