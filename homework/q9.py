noOfApple = int(input())
noOfKiwi = int(input())
noOfPineApple = int(input())

priceOfApple = 30 * noOfApple
priceOfKiwi = 70 * noOfKiwi
priceOfPineApple = 40 * noOfPineApple

discountedPriceOfApple = (
    priceOfApple if noOfApple < 11
    else priceOfApple * 0.95 if noOfApple < 16
    else priceOfApple * 0.9 if noOfApple < 21
    else priceOfApple * 0.8
)
discountedPriceOfKiwi = (
    priceOfKiwi if noOfKiwi < 11
    else priceOfKiwi * 0.9 if noOfKiwi < 16
    else priceOfKiwi * 0.85 if noOfKiwi < 21
    else priceOfKiwi * 0.75
)
discountedPriceOfPineApple = (
    priceOfPineApple if noOfPineApple < 11
    else priceOfPineApple * 0.85 if noOfPineApple < 16
    else priceOfPineApple * 0.8 if noOfPineApple < 21
    else priceOfPineApple * 0.8
)

totalPrice = (
    discountedPriceOfApple +
    discountedPriceOfKiwi + discountedPriceOfPineApple
)
discountedTotalPrice = (
    totalPrice if noOfApple + noOfKiwi + noOfPineApple < 30
    else totalPrice * 0.87
)

print(int(discountedTotalPrice))
