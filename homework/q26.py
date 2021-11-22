from functools import reduce
from typing import List

Desk = List[str]


def countPoints(desk: Desk):
    return reduce(lambda accumulator, card: accumulator + (
        1 if card == 'A'
        else 0.5 if card in ('J', 'K', 'Q')
        else int(card)
    ), desk, 0.0)


def wonGameAlready(desk: Desk):
    return len(desk) == 5 or (
        '10' in desk and any(card in desk for card in ['J', 'Q', 'K'])
    )


def main():
    noOfPlayers = int(input())
    dealingPoints = list(map(lambda s: int(s), input().split(' ')))
    bankDesk: Desk = []
    playerDesks: list[Desk] = [[] for _ in range(noOfPlayers)]
    bankWonCredits: int = 0

    for index, card in enumerate(input().split(' ')):
        playerDesks[index].append(card)

    for index in range(noOfPlayers):
        desk = playerDesks[index]
        while not wonGameAlready(desk):
            choice = input()
            if choice == 'N':
                break
            desk.append(input())

    bankDesk.append(input())
    while not wonGameAlready(bankDesk):
        choice = input()
        if choice == 'N':
            break
        bankDesk.append(input())

    bankPoints = countPoints(bankDesk)
    for index, desk in enumerate(playerDesks):
        points = countPoints(desk)
        playerWonCredits = dealingPoints[index]

        if points <= 10.5 and (points > bankPoints or wonGameAlready(desk)):
            print(f'Player{index + 1} +{playerWonCredits}')
            bankWonCredits -= playerWonCredits
        else:
            print(f'Player{index + 1} -{playerWonCredits}')
            bankWonCredits += playerWonCredits

    sign = '+' if bankWonCredits > 0 else ''
    print(f'Bank {sign}{bankWonCredits}')


main()
