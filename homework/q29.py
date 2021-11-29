def main():
    array = list(map(lambda s: int(s), input().split(' ')))
    odd_numbers = [i for i in array if i % 2 == 1]
    even_numbers = [j for j in array if j % 2 == 0]
    odd_numbers.sort()
    even_numbers.sort(reverse=True)

    print(odd_numbers + even_numbers)


main()
