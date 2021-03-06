from functools import reduce
from typing import List

Desk = List[str]


def countPoints(desk: Desk):
    return reduce(lambda accumulator, card: accumulator + (
        1 if card == 'A'
        else 0.5 if card in ('J', 'K', 'Q')
        else int(card)
    ), desk, 0.0)


def wonGame(desk: Desk):
    return len(desk) == 5 or (
        '10' in desk and any(card in desk for card in ['J', 'Q', 'K'])
    )


def inputCard(desk: Desk):
    while countPoints(desk) <= 10.5 and not wonGame(desk):
        choice = input()
        if choice == 'N':
            break
        desk.append(input())


def main():
    noOfPlayers = int(input())
    dealingPoints = list(map(lambda s: int(s), input().split(' ')))
    bankDesk: Desk = []
    playerDesks: list[Desk] = [[] for _ in range(noOfPlayers)]
    bankWonCredits: int = 0

    for index, card in enumerate(input().split(' ')):
        playerDesks[index].append(card)

    for index in range(noOfPlayers):
        inputCard(playerDesks[index])

    bankDesk.append(input())
    inputCard(bankDesk)

    bankPoints = countPoints(bankDesk)
    for index, desk in enumerate(playerDesks):
        points = countPoints(desk)
        bet = dealingPoints[index]

        if points <= 10.5 and (bankPoints > 10.5 or wonGame(desk) or points > bankPoints):
            print(f'Player{index + 1} +{bet}')
            bankWonCredits -= bet
        else:
            print(f'Player{index + 1} -{bet}')
            bankWonCredits += bet

    print(f'Bank {"+" if bankWonCredits > 0 else ""}{bankWonCredits}')


main()
