def main():
    s = input()

    lowerChars = ''
    upperCount = 0

    for c in s:
        if c.islower():
            lowerChars += c
        elif c.isupper():
            upperCount += 1

    print(lowerChars if len(lowerChars) > 0 else 'No lowercase letters')
    print(len(s))
    print(upperCount)


main()
