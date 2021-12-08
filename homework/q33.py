from typing import List
from functools import reduce


def gcd(x: int, y: int) -> int:
    while (x > 0) and (y > 0):
        if (x > y):
            x = x % y
        else:
            y = y % x
    return (x if x > y else y)


def multipleGcd(arr: List[int]):
    return reduce(lambda a, b: gcd(a, b), arr[1:], arr[0])


def main():
    result: List[int] = []

    while True:
        inp = input()
        if inp == '-1':
            break
        result.append(multipleGcd(list(map(lambda s: int(s), inp.split(' ')))))

    print('\n'.join(map(str, result)))


main()
