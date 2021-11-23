from typing import List, Tuple


def passwordStrength(password: str):
    points = 0
    digitCount = 0
    haveConsecutiveDigits = False

    for index, char in enumerate(password):
        if char.islower():
            points += 1
        elif char.isupper():
            points += 2
        elif char.isdecimal():
            points += 3
            digitCount += 1
            if index + 1 < len(char) and password[index + 1].isdecimal():
                haveConsecutiveDigits = True
        elif char in ["~", "!", "@", "#", "$", "%", "^", "&", "*", "<", ">", "_", "+", "="]:
            points += 5

    if digitCount >= 5 and not haveConsecutiveDigits:
        points += 10

    return points


def main():
    results: List[Tuple[str, int]] = []

    while True:
        inp = input()
        if inp == '-1':
            break
        results.append((inp, passwordStrength(inp)))

    results.sort(key=lambda result: result[1], reverse=True)

    print(f'{results[0][0]} {results[0][1]}')
    print(f'{results[-1][0]} {results[-1][1]}')


main()
