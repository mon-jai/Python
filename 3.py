def myPrint01():
    for i in range(0, 10, 1):
        print(i)


def myPrint02(m, n):
    for j in range(m, n, -1):
        print(j, end='')  # 不換行


def myPrint03(m):
    for j in range(0, 2*m-1, 1):
        print(j, end='')  # 不換行


def main():
    num = 5
    myPrint01()
    myPrint02(num, 8)
    myPrint03(num)
    print()  # 預設換行


main()
