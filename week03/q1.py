try:
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
except ValueError:
    print("Input Integer")
except ZeroDivisionError:
    print("divide by zero")
finally:
    print("OK")
