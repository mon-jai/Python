def calculate(number: int) -> int:
    return 2 if number == 1 else calculate(number - 1) + number


print(calculate(int(input())), end='')
