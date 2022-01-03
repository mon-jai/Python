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


def is_two_city_connected(
    city_to_check: int,
    checkpoint: int,
    destination: int,
    relationship_graph: Relationship_Graph,
    cities_passed_through: List[int] = []
) -> List[int]:
    if city_to_check in cities_passed_through:
        return []

    relationship_of_the_city_being_checked = relationship_graph[city_to_check]

    cities_passed_through.append(city_to_check)

    if destination in relationship_of_the_city_being_checked and checkpoint in cities_passed_through:
        cities_passed_through.append(destination)
        return cities_passed_through
    else:
        possible_paths: List[List[int]] = []
        for connected_city in relationship_of_the_city_being_checked:
            path_to_city = is_two_city_connected(connected_city, checkpoint, destination, relationship_graph, cities_passed_through.copy())

            if len(path_to_city) > 0:
                possible_paths.append(path_to_city)

        if len(possible_paths) == 0:
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

    print(is_two_city_connected(starting_point, checkpoint, destination, relationship_graph))


main()
