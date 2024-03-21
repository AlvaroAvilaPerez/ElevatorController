from sistema.floor import Floor


def test_call_elevator():
    floor = Floor(floor_number=1, elevator=None)
    floor.call_elevator(True)
    assert floor.up_button == False

