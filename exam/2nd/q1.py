from itertools import chain, combinations
from functools import reduce
from typing import Any, Dict, List, Tuple, Iterable


def powerset(iterable: Iterable[Any]) -> Iterable[Tuple[Any, ...]]:
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def main():
    buffer: Dict[int, List[Tuple[int, ...]]] = {}

    inputs = input()
    inputedNumbers = list(map(lambda s: int(s), inputs.split(' ')))

    for tuple in powerset(inputedNumbers):
        index = reduce(lambda i, j: i*j, tuple)

        if not index in buffer:
            buffer[index] = []
        buffer[index].append(tuple)

    print(buffer)


main()
