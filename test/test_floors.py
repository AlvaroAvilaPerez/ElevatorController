from System.floors import Floor

def test_call_elevator():
    floor = Floor(floor_number=1, elevator=None)
    floor.call_elevator(above=False)
    assert floor.above_button == False
