matrix: list[list[list[str]]] = [[[] for _ in range(9)] for _ in range(5)]


def inputCourse():
    courseCode = input()
    noOfHours = int(input())

    for _ in range(noOfHours):
        weekday, section = [int(s) for s in list(input())]
        matrix[weekday - 1][section - 1].append(courseCode)


def output():
    for weekday, weekdayList in enumerate(matrix):
        for section, sectionList in enumerate(weekdayList):
            if len(sectionList) > 1:
                print(
                    f'{sectionList[0]} and {sectionList[1]} conflict on {weekday + 1}{section + 1}'
                )
                return


for i in range(3):
    inputCourse()
