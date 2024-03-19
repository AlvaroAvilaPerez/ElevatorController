from ascensor import Elevator
from botonDePiso import FloorButton

def test_go_up_floor():
    floor_button = FloorButton(0)
    elevator_t = Elevator([floor_button])
    result = elevator_t.go_up_floor()
    assert elevator_t.current_floor == 1
