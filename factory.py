class Controller:
    def __init__(self,map, initial_park):
        self.vehicles = initial_park
        self.vehicles_on_rest = initial_park #suppose that all vehicles rest when class is made
        self.vehicles_on_maintenance = []
        self.map = map

    def send_car_to_maintainance(self, vehicle):
        pass
    def send_car_to_rest(self, vehicle):
        pass
    def send_car_to_act(self, vehicle, tunnel):
        pass




class Vehicle:
    def __init__(self, coordinates, status, current_target_path):
        super().__init__()
        self.coordinates = coordinates
        self.status = status  # "pause" or "moving" or "acting" or "maintenance"
        self.current_target_path = current_target_path # may be None

    def Move(self, path):
        self.current_target_path = path
        self.status = "moving"
        pass

    def Act(self):
        pass


class Vehicle_Drill(Vehicle):
    def __init__(self, coordinates, status, current_target_path):
        super().__init__(coordinates, status, current_target_path)

    def Act(self):
        #Drill, baby, Drill! Quote - Trump during inauguration
        pass;


class Vehicle_Mapper(Vehicle):
    def __init__(self, coordinates, status, current_target_path):
        super().__init__(coordinates, status, current_target_path)

    def Act(self):
        #Я карта!
        pass;


class Vehicle_Checker(Vehicle):
    def __init__(self, coordinates, status, current_target_path):
        super().__init__(coordinates, status, current_target_path)
        self.damaged_tunnel_percentages = {} #Запись инфы о проверенных туннелях, о повреждении креплениий в конкретных туннелях

    def Act(self):
        #Check tunnel connections!
        pass;


class Tunnel:
    def __init__(self, start_position, end_position, connections):
        self.start_position = start_position
        self.end_position = end_position
        self.connections = connections # {"Arc":0%, "Trapeceidal":5%} Stores connection type data


class Path:
    def __init__(self):
        self.tunnels = []


class Map:
    def __init__(self, paths):
        self.paths = paths #list of path lists
    def BuildPath(self, Tunnel_A, Tunnel_B) -> Path:
        pass
    def UpdateTunnelInfo(self, tunnel, connectionType, damage_percentage):
        pass
