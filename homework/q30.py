def main():
    words = input().split(' ')
    keys = list(map(lambda s: int(s), input().split(' ')))
    dictionary = dict(zip(keys, words))

    keys.sort()
    print(''.join([dictionary[key] for key in keys]))


main()
