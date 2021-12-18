from typing import List, Tuple


def main():
    data: List[Tuple[int, int]] = []

    for _ in range(int(input())):
        numbers = [int(s) for s in input().split(',')]
        data.append((numbers[0], numbers[1]))

    while True:
        merged = False
        for index1, tuple1 in enumerate(data):
            for tuple2 in data:
                if (
                    id(tuple2) != id(tuple1) and
                    tuple1[0] <= tuple2[0] <= tuple1[1]
                ):
                    data.remove(tuple2)
                    data[index1] = (min(tuple1[0], tuple2[0]),
                                    max(tuple1[1], tuple2[1]))
                    merged = True
        if not merged:
            break

    print('\n'.join([f'{tuple[0]},{tuple[1]}' for tuple in data]))


main()
