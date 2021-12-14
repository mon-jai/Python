from typing import List, Tuple

Data = List[Tuple[int, int]]


def merge(data: Data) -> Data:
    result = [tuple for tuple in data]
    merged = False

    for index1, tuple1 in enumerate(result):
        for tuple2 in result:
            if (
                id(tuple2) != id(tuple1) and
                tuple1[0] <= tuple2[0] <= tuple1[1]
            ):
                result.remove(tuple2)
                result[index1] = (min(tuple1[0], tuple2[0]),
                                  max(tuple1[1], tuple2[1]))
                merged = True

    return result if merged == False else merge(result)


def main():
    data: Data = []

    for _ in range(int(input())):
        numbers = [int(s) for s in input().split(',')]
        data.append((numbers[0], numbers[1]))

    print('\n'.join([f'{tuple[0]},{tuple[1]}' for tuple in merge(data)]))


main()
