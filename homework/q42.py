from typing import Callable, List, Union, cast

Arithmetic_Sequence = List[Union[str, float]]
Operation = Callable[[Union[str, float], Union[str, float]], float]


def parse_arithmetic_expression(expression: str) -> Arithmetic_Sequence:
    arithmetic_sequence: List[str] = []

    for char in expression:
        if char == ' ':
            continue
        elif char.isdigit():
            if len(arithmetic_sequence) == 0 or not arithmetic_sequence[-1].isdigit():
                arithmetic_sequence.append(char)
            else:
                arithmetic_sequence[-1] = arithmetic_sequence[-1] + char
        else:
            # Arithmetic symbols
            arithmetic_sequence.append(char)

    return cast(Arithmetic_Sequence, arithmetic_sequence)


def calculate(arithmetic_sequence: Arithmetic_Sequence) -> float:
    addition: Operation = lambda s1, s2: int(s1) + int(s2)
    subtraction: Operation = lambda s1, s2: int(s1) - int(s2)
    multiplication: Operation = lambda s1, s2: int(s1) * int(s2)
    division: Operation = lambda s1, s2: int(s1) / int(s2)
    modulus: Operation = lambda s1, s2: int(s1) % int(s2)

    def sub_calculate(index: int):
        operation = (
            addition if arithmetic_sequence[index] == '+'
            else subtraction if arithmetic_sequence[index] == '-'
            else multiplication if arithmetic_sequence[index] == '*'
            else division if arithmetic_sequence[index] == '/'
            else modulus
        )

        arithmetic_sequence[index - 1] = operation(arithmetic_sequence[index - 1],arithmetic_sequence[index + 1])
        del arithmetic_sequence[index + 1]
        del arithmetic_sequence[index]

    while True:
        if '*' in arithmetic_sequence:
            sub_calculate(arithmetic_sequence.index('*'))
            continue
        elif '/' in arithmetic_sequence:
            sub_calculate(arithmetic_sequence.index('/'))
            continue
        else:
            break

    while True:
        if '+' in arithmetic_sequence:
            sub_calculate(arithmetic_sequence.index('+'))
            continue
        elif '-' in arithmetic_sequence:
            sub_calculate(arithmetic_sequence.index('-'))
            continue
        else:
            break

    return cast(float, arithmetic_sequence[0])


print(calculate(parse_arithmetic_expression(input())))
