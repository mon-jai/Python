def getPrice(userInputs: list[int], plan: list[float]) -> float:
    return sum([userInput * plan[index] for index, userInput in enumerate(userInputs)])


def main():
    plan183 = [0.08, 0.1393, 0.1349, 1.1287, 1.4803]
    plan383 = [0.07, 0.1304, 0.1217, 1.1127, 1.2458]

    userInputs = [int(input()) for _ in range(5)]

    plan183Price = getPrice(userInputs, plan183)
    plan383Price = getPrice(userInputs, plan383)
    print(plan183Price)
    print(plan383Price)

    if (plan183Price <= 183):
        print('Type 183')
    elif (plan383Price <= 383):
        print('Type 383')
    else:
        print('Type 983')


main()
