from typing import Dict, Tuple


def filter_colleges(colleges_to_characteristics: Dict[str, Tuple[str, ...]], requirements: str):
    result: Dict[str, int] = {}

    for college, characteristics in colleges_to_characteristics.items():
        matches = 0

        for requirement_group in [s.strip() for s in requirements.split('+')]:
            match = True

            for requirement in [s.strip() for s in requirement_group.split(' ')]:
                if requirement.startswith('!'):
                    if requirement[1:] in characteristics:
                        match = False
                        break
                else:
                    if requirement not in characteristics:
                        match = False
                        break

            if match:
                matches += 1

        if matches > 0:
            result[college] = matches

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


def main():
    colleges_to_characteristics: Dict[str, Tuple[str, ...]] = {}

    no_of_colleges = int(input())
    for _ in range(no_of_colleges):
        college, *characteristics = input().split(' ')
        colleges_to_characteristics[college] = tuple(characteristics)

    requirements = input()

    print(' '.join([
        f'{college},{matches}'
        for college, matches in filter_colleges(colleges_to_characteristics, requirements).items()
    ]))


main()
