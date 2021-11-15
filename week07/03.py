from typing import Callable

def isPrime(x: int):
    isPrimeNumber: Callable[[int], bool] = lambda num: not any(
        [num % i == 0 for i in range(2, num)]
    )
    ans = 0
    for i in range(1, x+1):
        if isPrimeNumber(i):
            ans += i
    print(ans)
