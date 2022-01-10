from typing import NamedTuple, Set, Iterable, List
from itertools import combinations


class Meeting(NamedTuple):
    id: int
    hour_occupied: Set[int]


def get_set_of_hours_from_time(starting_time: int, ending_time: int):
    return set(range(starting_time, ending_time))


def sum_of_meeting_length(meetings: Iterable[Meeting]):
    return sum(map(lambda meeting: len(meeting.hour_occupied), meetings))


def main():
    no_of_rooms, no_of_meetings = [int(s) for s in input().split()]
    meetings: List[Meeting] = []

    for _ in range(no_of_meetings):
        meeting_id, starting_time, ending_time = [int(s) for s in input().split()]
        meetings.append(Meeting(meeting_id, get_set_of_hours_from_time(starting_time, ending_time)))

    meetings_combinations = [
        meetings_combination
        for i in range(1, no_of_meetings + 1)
        for meetings_combination in combinations(meetings, i)
        if all(
            len(meeting_a.hour_occupied & meeting_b.hour_occupied) == 0
            for meeting_a, meeting_b in combinations(meetings_combination, 2)
        )
    ]

    meetings_combinations.sort(key=sum_of_meeting_length, reverse=True)

    selected_meetings: list[Meeting] = []

    for _ in range(no_of_rooms):
        selected_meetings += [meeting for meeting in meetings_combinations[0]]
        del meetings_combinations[0]

        meetings_combinations = list(filter(
            lambda meetings_combination: all(meeting not in selected_meetings for meeting in meetings_combination),
            meetings_combinations
        ))

    print(sum_of_meeting_length(selected_meetings))


main()
