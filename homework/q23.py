from typing import List
from functools import reduce


def main():
    computerCards: List[str] = []
    playerCards: List[str] = []

    computerGaveup = False
    playerGaveup = False

    def calculatePoints(cards: List[str]) -> float:
        points = reduce(
            lambda count, card: count + (
                1 if card == "A"
                else 0.5 if card in ("J", "K", "Q")
                else int(card)
            ), cards, 0.0
        )
        return points if points <= 10.5 else 0

    def willPlayerDealsCard():
        nonlocal playerGaveup

        if calculatePoints(playerCards) == 0:
            return False
        elif playerGaveup == True:
            return False
        else:
            if input() == 'N':
                playerGaveup = True
                return False
            else:
                return True

    def willComputerDealsCard():
        nonlocal computerGaveup
        computerPoints = calculatePoints(computerCards)
        computerGaveup = not (
            computerPoints < calculatePoints(playerCards) or computerPoints < 8
        )

        return not computerGaveup and computerPoints != 0 and calculatePoints(playerCards) != 0

    playerCards.append(input())
    computerCards.append(input())

    while True:
        playerDealsCard = willPlayerDealsCard()
        if playerDealsCard:
            playerCards.append(input())

        computerDealsCard = willComputerDealsCard()
        if computerDealsCard:
            computerCards.append(input())

        if not playerDealsCard and not computerDealsCard:
            break

    playerPoints = calculatePoints(playerCards)
    computerPoints = calculatePoints(computerCards)

    print(f'{playerPoints:.1f} vs. {computerPoints:.1f}')
    print(
        'player wins' if playerPoints > computerPoints
        else 'computer wins' if computerPoints > playerPoints
        else "It's a tie"
    )


main()
