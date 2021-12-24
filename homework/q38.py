from math import floor


def main():
    input_string = 'abbabcc'
    result: list[str] = []

    for i in range(len(input_string)):
        print(i)
        for j in range(i, len(input_string)):
            substring = input_string[i:j + 1]
            print(substring)
            ok = True

            for k in range(floor(len(substring) / 2)):
                if substring[k] != substring[-(k + 1)]:
                    ok = False
                    break

            if ok:
                result.append(substring)

    print(sorted(result))


main()
