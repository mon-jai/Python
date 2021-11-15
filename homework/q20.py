num = int(input())

if not any([num % i == 0 for i in range(2, num)]):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")
