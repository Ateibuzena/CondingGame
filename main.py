import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# main.py

# Definición de clases
class SeleniaCity:
    def __init__(self, resources, travel_routes, transport_pods, new_buildings):
        self.resources = resources
        self.travel_routes = travel_routes
        self.transport_pods = transport_pods
        self.new_buildings = new_buildings

class TravelRoute:
    def __init__(self, building_id1, building_id2, capacity):
        self.building_id1 = building_id1
        self.building_id2 = building_id2
        self.capacity = capacity

class TransportPod:
    def __init__(self, pod_id, num_stops, path):
        self.pod_id = pod_id
        self.num_stops = num_stops
        self.path = path

class NewBuilding:
    def __init__(self, data):
        self.building_type = data["building_type"]
        self.building_id = data["building_id"]
        self.coord_x = data["coord_x"]
        self.coord_y = data["coord_y"]
        self.num_astronauts = data["num_astronauts"] or None
        self.astronaut_types = data["astronaut_types"] or None

def create_city_from_input():
    resources = int(input())  # Leer recursos
    num_travel_routes = int(input())  # Leer número de rutas
    travel_routes = []

    # Leer las rutas de viaje
    for _ in range(num_travel_routes):
        building_id1, building_id2, capacity = map(int, input().split())
        travel_routes.append(TravelRoute(building_id1, building_id2, capacity))

    num_pods = int(input())  # Leer número de cápsulas
    transport_pods = []

    # Leer las cápsulas de transporte
    for _ in range(num_pods):
        pod_data = list(map(int, input().split()))
        pod_id = pod_data[0]
        num_stops = pod_data[1]
        path = pod_data[2:2 + num_stops]
        transport_pods.append(TransportPod(pod_id, num_stops, path))

    num_new_buildings = int(input())  # Leer número de nuevos edificios
    building_dic = {"building_type" : 0,
                    "building_id" : 0,
                    "coord_x" : 0,
                    "coord_y" : 0,
                    "num_astronauts" : 0,
                    "astronaut_types" : 0
                    }
    new_buildings = []
    # Leer nuevos edificios (no se utiliza en esta versión, pero se puede almacenar si es necesario)
    for _ in range(num_new_buildings):
        building_data = list(map(int, input().split()))
        building_dic["building_type"] = building_data[0]
        building_dic["building_id"] = building_data[1]
        building_dic["coord_x"] = building_data[2]
        building_dic["coord_y"] = building_data[3]

        if building_dic["building_type"] > 0:
            building_dic["num_astronauts"] = None  # o usar "" para dejar vacío
            building_dic["astronaut_types"] = None  # o usar "" para dejar vacío
        else:
            building_dic["num_astronauts"] = building_data[4]
            building_dic["astronaut_types"] = building_data[5]

        new_buildings.append(NewBuilding(building_dic))


    return resources, travel_routes, transport_pods

def plan_actions(resources, travel_routes, transport_pods, new_buildings):
    actions = []

    # Ejemplo: crear tubos entre edificios si hay recursos suficientes
    for route in travel_routes:
        if route.capacity > 0:  # Solo si hay capacidad disponible
            distance = 1  # Asumimos una distancia ficticia; deberías calcular la real
            cost = int(distance // 0.1)  # Costo en recursos
            if resources >= cost:
                actions.append(f"TUBE {route.building_id1} {route.building_id2}")
                resources -= cost  # Restar recursos después de la acción
        elif route.capacity == 0:
            distance = 1
            cost = 5000
            if resources >= cost:
                actions.append(f"TELEPORT {route.building_id1} {route.building_id2}")
                resources -= cost  # Restar recursos después de la acción

    # Ejemplo: crear cápsulas de transporte
    for pod in transport_pods:
        if resources >= 1000:  # Comprobar si hay recursos suficientes para crear una cápsula
            actions.append(f"POD {pod.pod_id} {' '.join(map(str, pod.path))}")
            resources -= 1000  # Restar recursos después de la acción

    return actions

# Bucle principal del juego
while True:
    # Crear la ciudad y obtener información
    resources, travel_routes, transport_pods, new_buildings = create_city_from_input()

    # Planificar acciones basadas en la información
    actions = plan_actions(resources, travel_routes, transport_pods)

    # Si no se generaron acciones, imprimir "WAIT"
    if not actions:
        print("WAIT")
    else:
        print(";".join(actions))  # Imprimir las acciones separadas por punto y coma
