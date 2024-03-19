from sistema.configurationBuilding import Setting


class Tower:
    """Esta clase es una representación de un edificio con un número específico de pisos y ascensores"""
    def __init__(self, floor, elevator):
        self.floors = floor
        self.elevators = elevator


tower_building = Setting(20, 3)
tower_building.floors[0].call_elevator(up=True)
tower_building.elevators[0].go_to_floor(15)
tower_building.elevators[0].go_to_floor(5)
tower_building.elevators[2].go_to_floor(2)
tower_building.elevators[3].go_to_floor(1)
tower_building.elevators[1].go_to_floor(12)
elevator_nearby = tower_building.get_elevator_plus_nearby(5)
