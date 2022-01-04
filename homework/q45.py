from collections import defaultdict
from typing import Dict, List, Tuple

Connections = List[Tuple[int, int]]
Connection_Graph = Dict[int, List[int]]


def build_connection_graph(connections: Connections):
    connection_graph: Connection_Graph = defaultdict(list)

    for connection in connections:
        first_city, second_city = connection
        connection_graph[first_city].append(second_city)
        connection_graph[second_city].append(first_city)

    return connection_graph


def path_to_destination(
    starting_point: int,
    checkpoint: int,
    destination: int,
    connection_graph: Connection_Graph
) -> List[int]:
    possible_paths: List[List[int]] = [[starting_point]]

    while True:
        # https://stackoverflow.com/a/3752697
        # https://stackoverflow.com/a/6260097
        for path in possible_paths.copy():
            current_city = path[-1]
            possible_paths.remove(path)
            is_dead_end = True

            for connected_city in connection_graph[current_city]:
                if destination == connected_city and checkpoint in path:
                    path.append(destination)
                    return path
                elif connected_city not in path:
                    possible_paths.append(path + [connected_city])
                    is_dead_end = False

            if is_dead_end:
                return []


def main():
    no_of_connections, starting_point, checkpoint, destination = [int(s) for s in input().split()]
    connections: Connections = []

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
