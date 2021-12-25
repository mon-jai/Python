from math import floor


def main():
    input_string = input()
    result: list[str] = []

    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            substring = input_string[i:j + 1]
            if all([substring[k] == substring[-(k + 1)]
                    for k in range(floor(len(substring) / 2))]):
                result.append(substring)

    print('#'.join(sorted(list(dict.fromkeys(result)))))


main()
