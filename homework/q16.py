def main():
    name = input()
    height = int(input()) / 100
    weight = int(input())

    bmi = weight / height ** 2
    comment = (
        " too HIGH" if bmi > 24
        else " too LOW" if bmi < 18.5
        else ""
    )

    print(
        f'Hi {name}, Your BMI: {bmi:.6f}{comment}.'
    )


main()
