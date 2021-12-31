from typing import Dict, List, Tuple


Relationship_Graph = Dict[int, List[int]]


def build_relationship_graph(relationships: List[Tuple[int, int]]):
    relationship_graph: Relationship_Graph = {}

    for relationship in relationships:
        first_person, second_person = relationship

        if first_person not in relationship_graph:
            relationship_graph[first_person] = []

        if second_person not in relationship_graph:
            relationship_graph[second_person] = []

        relationship_graph[first_person].append(second_person)
        relationship_graph[second_person].append(first_person)

    return relationship_graph


def is_two_person_connected(
    person_to_check: int,
    person_to_find: int,
    relationship_graph: Relationship_Graph,
    checked: List[int] = []
):
    if person_to_check in checked:
        return False

    relationship_of_the_person_being_checked = relationship_graph[person_to_check]

    if person_to_find in relationship_of_the_person_being_checked:
        return True
    else:
        checked.append(person_to_check)

        for connected_person in relationship_of_the_person_being_checked:
            if is_two_person_connected(
                connected_person,
                person_to_find,
                relationship_graph,
                checked
            ):
                return True

        return False


def main():
    no_of_relationships, person_to_start, person_to_find = [
        int(s) for s in input().split()
    ]

    relationships: List[Tuple[int, int]] = []

    for _ in range(no_of_relationships):
        person_a, person_b = [int(s) for s in input().split()]
        relationships.append((person_a, person_b))

    relationship_graph = build_relationship_graph(relationships)

    print(
        'Yes!' if is_two_person_connected(
            person_to_start,
            person_to_find,
            relationship_graph
        )
        else 'No!'
    )


main()
