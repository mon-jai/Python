def myPrintS():
    print('1 ', end="")
    for i in range(1, 4):
        print('2 ', end="")
        for j in range(i):
            print('3 ', end="")
            print('4 ', end='')
        print('5 ', end='')

myPrintS()