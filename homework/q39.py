from functools import cmp_to_key
from itertools import combinations
from typing import Callable


def main():
    inputs = input().split(' ')
    string, length = inputs[0], int(inputs[1])

    comparer: Callable[[str, str], int] = lambda a, b: (
        1 if string.index(a) > string.index(b) else -1
    )
    print(string, length)
    combs = sorted([
        ''.join(sorted(comb, key=cmp_to_key(comparer)))
        for comb in combinations(string, length)
        if comb[0] != comb[1] and comb[0] != comb[2] and comb[1] != comb[2]
    ])

    print(' '.join(combs))


main()
