def getPrice(userInputs: list[int], rent: int, plan: list[float]) -> float:
    fee = sum([userInput * plan[index]
              for index, userInput in enumerate(userInputs)])

    if fee == 0 or fee < rent:
        return rent
    else:
        return fee - rent


def main():
    plan183 = [0.08, 0.1393, 0.1349, 1.1287, 1.4803]
    plan383 = [0.07, 0.1304, 0.1217, 1.1127, 1.2458]
    plan983 = [0.06, 0.1087, 0.1018, 0.9572, 1.1243]

    userInputs = [int(input()) for _ in range(5)]

    plan183Price = getPrice(userInputs, 183, plan183)
    plan383Price = getPrice(userInputs, 383, plan383)
    plan983Price = getPrice(userInputs, 983, plan983)

    if (plan183Price < plan383Price and plan183Price < plan983Price):
        print('Type 183')
    elif ( plan383Price < plan983Price):
        print('Type 383')
    elif (plan983Price < plan183Price and plan983Price < plan383Price):
        print('Type 983')
    else:
        print('')


main()
