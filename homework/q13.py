def calculate():
    a = int(input())
    b = int(input())

    c = 0
    d = 1

    for i in range(a, b + 1, 2):
        c += i

    for i in range(a, b + 1, 3):
        d *= i

    print(c)
    print(d)


calculate()
