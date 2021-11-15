def main():
    n = int(input())
    inp: list[int] = []

    for i in range(n):
        inp += [int(input())]

    inp.sort(reverse=True)

    print(inp[1])
    print(inp[0] * inp[-1])


main()
