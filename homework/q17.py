import math


def right(noOfLines: int):
    for i in range(1, noOfLines + 1):
        if i / (noOfLines + 1) <= 0.5:
            print('*' * i)
        else:
            print('*' * (noOfLines + 1 - i))


def left(noOfLines: int):
    width = math.ceil(noOfLines / 2)
    for i in range(1, noOfLines + 1):
        if i / (noOfLines + 1) <= 0.5:
            print('.' * (width - i), end='')
            print('*' * (i))
        else:
            noOfStar = noOfLines + 1 - i
            print('.' * (width - noOfStar), end='')
            print('*' * noOfStar)


def middle(noOfLines: int):
    width = math.ceil(noOfLines / 2)
    for i in range(1, noOfLines + 1):
        if i / (noOfLines + 1) <= 0.5:
            print('.' * (width - i), end='')
            print('*' * (i + (i - 1)))
        else:
            noOfStar = noOfLines + 1 - i
            print('.' * (width - noOfStar), end='')
            print('*' * (noOfStar + (noOfStar - 1)))


def main():
    type = int(input())
    noOfLines = int(input())
    handler = (
        right if type == 1
        else left if type == 2
        else middle
    )

    handler(noOfLines)


main()
