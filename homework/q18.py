from typing import Callable

printNumbers: Callable[[int], None] = lambda i: print(
    "".join([f'{j}' for j in range(1, i + 1)]), end=''
)
printNumbersReversed: Callable[[int], None] = lambda i: print(
    "".join([f'{k}' for k in range(i, 0, -1)]), end=''
)


def rightTriangle(noOfLines: int):
    for i in range(1, noOfLines + 1):
        printNumbers(i)
        printNumbersReversed(i - 1)
        print()


def triangle(noOfLines: int):
    for i in range(1, noOfLines + 1):
        print('_' * (noOfLines - i), end='')
        printNumbers(i)
        printNumbersReversed(i - 1)
        print('_' * (noOfLines - i))


def reversedTriangle(noOfLines: int):
    for i in range(noOfLines, 0, -1):
        print('_' * (noOfLines - i), end='')
        printNumbers(i)
        printNumbersReversed(i - 1)
        print('_' * (noOfLines - i))


def main():
    type = int(input())
    noOfLines = int(input())
    handler = (
        rightTriangle if type == 1
        else triangle if type == 2
        else reversedTriangle
    )

    handler(noOfLines)


main()
