from collections import defaultdict
from typing import Dict, List, Tuple

Relationships = List[Tuple[int, int]]
Relationship_Graph = Dict[int, List[int]]


def build_connection_graph(connections: Relationships):
    connection_graph: Relationship_Graph = defaultdict(list)

    for connection in connections:
        first_city, second_city = connection
        connection_graph[first_city].append(second_city)
        connection_graph[second_city].append(first_city)

    return connection_graph


def path_to_destination(
    city_to_check: int,
    checkpoint: int,
    destination: int,
    connection_graph: Relationship_Graph,
    cities_passed_through: List[int] = [],
    dead_ends: List[int] = []
) -> List[int]:
    if city_to_check in cities_passed_through or city_to_check in dead_ends:
        return []

    connected_cities = connection_graph[city_to_check]

    cities_passed_through.append(city_to_check)

    if destination in connected_cities and checkpoint in cities_passed_through:
        cities_passed_through.append(destination)
        return cities_passed_through
    else:
        possible_paths = [
            path for path in map(
                lambda connected_city: path_to_destination(connected_city, checkpoint, destination, connection_graph, cities_passed_through.copy(), dead_ends),
                connected_cities
            )
            if len(path) > 0
        ]

        if len(possible_paths) == 0:
            dead_ends.append(city_to_check)
            return []
        else:
            possible_paths.sort(key=len)
            return possible_paths[0]


def main():
    no_of_connections, starting_point, checkpoint, destination = [int(s) for s in input().split()]
    connections: Relationships = []

    for _ in range(no_of_connections):
        city_a, city_b = [int(s) for s in input().split()]
        connections.append((city_a, city_b))

    connection_graph = build_connection_graph(connections)
    path = path_to_destination(starting_point, checkpoint, destination, connection_graph)

    if len(path) > 0:
        print(len(path) - 1)
        print('-'.join(str(city) for city in path))
    else:
        print('No way!')


main()
