from functools import cmp_to_key
from itertools import combinations


def main():
    string, length = input().split(' ')
    length = int(length)

    def compare(a: str, b: str):
        return 1 if string.index(a) > string.index(b) else -1

    combs = sorted([
        ''.join(sorted(comb, key=cmp_to_key(compare)))
        for comb in combinations(string, length)
        if comb[0] != comb[1] and comb[0] != comb[2] and comb[1] != comb[2]
    ])

    print(' '.join(combs))


main()
