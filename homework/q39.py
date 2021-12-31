from functools import cmp_to_key
from itertools import combinations
from typing import Callable


def main():
    inputs = input().split(' ')
    string, length = inputs[0], int(inputs[1])

    comparer: Callable[[str, str], int] = lambda a, b: (
        1 if string.index(a) > string.index(b) else -1
    )
    combs = sorted([
        ''.join(sorted(comb, key=cmp_to_key(comparer)))
        for comb in combinations(string, length)
        if len(set(comb)) == len(comb)
    ])

    print(' '.join(combs))


main()
