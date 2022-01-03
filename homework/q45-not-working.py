from typing import Dict, List, Tuple

Relationships = List[Tuple[int, int]]
Relationship_Graph = Dict[int, List[int]]


def build_relationship_graph(relationships: Relationships):
    relationship_graph: Relationship_Graph = {}

    for relationship in relationships:
        first_city, second_city = relationship

        if first_city not in relationship_graph:
            relationship_graph[first_city] = []

        if second_city not in relationship_graph:
            relationship_graph[second_city] = []

        relationship_graph[first_city].append(second_city)
        relationship_graph[second_city].append(first_city)

    return relationship_graph


def path_to_destination(
    city_to_check: int,
    checkpoint: int,
    destination: int,
    relationship_graph: Relationship_Graph,
    cities_passed_through: List[int] = [],
    dead_ends: List[int] = []
) -> List[int]:
    if city_to_check in cities_passed_through or city_to_check in dead_ends:
        return []
    cities_passed_through.append(city_to_check)

    cities_connected = relationship_graph[city_to_check]
    if destination in cities_connected and checkpoint in cities_passed_through:
        cities_passed_through.append(destination)
        return cities_passed_through
    else:
        possible_paths: List[List[int]] = [
            path for path in map(
                lambda connected_city: path_to_destination(connected_city, checkpoint, destination, relationship_graph, cities_passed_through.copy(), dead_ends),
                cities_connected
            )
            if len(path) > 0
        ]

        if len(possible_paths) == 0:
            dead_ends.append(city_to_check)
            return []
        else:
            list_by_length = [(path, len(path)) for path in possible_paths]
            list_by_length.sort(key=lambda x: x[1])
            return list_by_length[0][0]


def main():
    no_of_relationships, starting_point, checkpoint, destination = [int(s) for s in input().split()]

    relationships: Relationships = []

    for _ in range(no_of_relationships):
        city_a, city_b = [int(s) for s in input().split()]
        relationships.append((city_a, city_b))

    relationship_graph = build_relationship_graph(relationships)

    print(path_to_destination(starting_point, checkpoint, destination, relationship_graph))


main()
