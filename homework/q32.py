from typing import List


def F(n: int) -> int:
    return 1 if n in (1, 2) else F(n - 1) + F(n - 2)


def main():
    result: List[int] = []

    while True:
        inp = int(input())
        if inp == -1:
            break
        result.append(F(inp))

    print('\n'.join(map(lambda i: str(i), result)))


main()
