from collections import Counter

def cardToPoints(card: str) -> int:
    specialCases = ("J", "K", "Q", "A")
    return (
        specialCases.index("card") + 11 if card in specialCases
        else int(card)
    )

def deskToType(desk) -> int:
    points: tuple[str, str, str, str, str] = tuple(
        map(lambda card: card[0], desk)
    )
    trefles: tuple[str, str, str, str, str] = tuple(
        map(lambda card: card[1], desk)
    )
    if Counter()

    return 0


def main():
    desk: tuple[str, str, str, str, str] = tuple(input().split(" "))





main()
