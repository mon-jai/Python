from typing import List, TypedDict
from collections import Counter


class Card(TypedDict):
    number: str
    suit: str


Deck = List[Card]


def isContinuous(desk: Deck):
    specialNumber = ('J', 'K', 'Q')
    numbers = sorted(map(lambda card: (
        1 if card['number'] == 'A'
        else specialNumber.index(card['number']) + 11 if card['number'] in specialNumber
        else int(card['number'])
    ), desk))
    previousNumber = numbers[0] if numbers[0] != 13 else 0
    for number in numbers[1:]:
        if number != previousNumber + 1:
            for i in range(13 - number, 13 + 1):
                try:
                    numbers.index(i)
                except:
                    return False
            return True
        elif number == 13:
            previousNumber = 0
        else:
            previousNumber = number
    return True


def main():
    desk: Deck = list(map(
        lambda cardstr: Card(number=cardstr[0:-1], suit=cardstr[-1]),
        input().split(' ')
    ))
    numberCounter = Counter(
        map(lambda card: card['number'], desk)
    ).most_common(2)
    suitCounter = Counter(map(lambda card: card['suit'], desk)).most_common(1)
    if suitCounter[0][1] == 5 and isContinuous(desk):
        print(8)
    elif numberCounter[0][1] >= 4:
        print(7)
    elif numberCounter[0][1] == 3 and numberCounter[1][1] == 2:
        print(6)
    elif suitCounter[0][1] == 5:
        print(5)
    elif isContinuous(desk):
        print(4)
    elif numberCounter[0][1] == 3:
        print(3)
    elif numberCounter[0][1] == 2 and numberCounter[1][1] == 2:
        print(2)
    elif numberCounter[0][1] == 2:
        print(1)
    else:
        print(0)


main()
