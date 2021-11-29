from typing import List, Tuple, Union


def C(m: int, count: int = 0) -> Tuple[Union[int, None], int]:
    return (
        (None, count) if m == 1 or m == 0
        else C(m // 2, count + 1) if m % 2 == 0
        else C((m + 1) // 2, count + 1)
    )


def R(m: str):
    return f'{C(int(m, 2))[1]:04b}'


def main():
    result: List[str] = []

    while True:
        inp = input()
        if int(inp) == -1:
            break
        result.append((R(inp)))

    print('\n'.join(result))


main()
