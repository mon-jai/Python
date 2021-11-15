def main():
    noOfLines = int(input())

    for i in range(noOfLines, 0, -1):
        print('#' * (noOfLines * 2 - i), end='')
        print(''.join([f'{j}' for j in range(i, 0, -1)]))


main()
