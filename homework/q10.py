def cardToPoints(card: str) -> float:
    return (
        1 if card == 'A'
        else 0.5 if card in ('J', 'K', 'Q')
        else int(card)
    )


def clculatePoints(first: float, second: float, third: float) -> float:
    totalPoints = first + second + third
    return totalPoints if totalPoints <= 10.5 else 0


a1 = cardToPoints(input())
a2 = cardToPoints(input())
a3 = cardToPoints(input())

b1 = cardToPoints(input())
b2 = cardToPoints(input())
b3 = cardToPoints(input())

a = clculatePoints(a1, a2, a3)
b = clculatePoints(b1, b2, b3)

print(a)
print(b)

if(a > b):
    print('A Win')
elif (b > a):
    print('B Win')
else:
    print('Tie')
