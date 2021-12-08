def K(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * K(n - 1) + 3 * K(n - 2)


def on_error():
    print('Error')


def main():
    try:
        inp = int(input())
        if (inp <= 1):
            on_error()
            return
        print(K(inp))
    except ValueError:
        on_error()


main()
