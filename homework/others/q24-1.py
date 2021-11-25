def isLadder(i: int):
    previousDigit = 0
    for char in str(i):
        digit = int(char)
        if digit < previousDigit:
            return False
        else:
            previousDigit = digit
    return True


def main():
    maxNumber = int(input())
    count = 0

    for i in range(1, maxNumber + 1):
        if isLadder(i):
            count += 1

    print(count)


main()
