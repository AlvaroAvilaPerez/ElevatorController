from configuracionEdificio import Setting


class Building:
    """Este constructor inicializa una instancia de la clase con información sobre los pisos y los ascensores"""
    def __init__(self, floors, elevators):
        self.floors = floors
        self.elevators = elevators


tower_building = Setting(20, 3)
tower_building.floors[0].call_elevator(above=True)
tower_building.elevators[0].go_to_floor(30)
tower_building.elevators[2].go_to_floor(2)
tower_building.elevators[3].go_to_floor(7)
elevator_nearby = tower_building.get_closest_elevator(5)