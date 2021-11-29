from functools import reduce
from typing import List


def chinese_remainder(n: List[int], a: List[int]):
    sum = 0
    prod = reduce(lambda acc, b: acc * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a: int, b: int):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    x1, y1, x2, y2, x3, y3 = map(lambda s: int(s), input().split(' '))
    print(chinese_remainder([x1, x2, x3], [y1, y2, y3]))


main()
