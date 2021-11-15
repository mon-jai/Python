def transferPoint(card):
    pork = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.5, 0.5, 0.5]
    index = pork.index(card)
    return points[index]


def getSum(x, y, z):
    return x + y + z


def compare(x, y):
    if (x > 10.5):
        x = 0
    if (y > 10.5):
        y = 0

    if(x > y):
        print('A WIN')
    elif (x < y):
        print('B WIN')
    else:
        print('TIE')


def main():
    a1 = transferPoint(input())
    a2 = transferPoint(input())
    a3 = transferPoint(input())
    b1 = transferPoint(input())
    b2 = transferPoint(input())
    b3 = transferPoint(input())
    compare(getSum(a1, a2, a3), getSum(b1, b2, b3))


main()
