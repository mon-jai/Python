from typing import List, Union
import re


def splitGroups(inp: str):
    groups: List[str] = []
    start = 0
    index = 0
    charToCapture: Union[str, None] = None
    bracketCount = 0

    while index <= len(inp):
        if charToCapture is None:
            if inp[index].isdigit():
                charToCapture = 'bracket'
            elif inp[index].isalpha():
                charToCapture = 'alpha'
            else:
                raise Exception(f'Wrong charactor :{inp[index]}')
        else:
            if index == len(inp) - 1:
                groups.append(inp[start:index + 1])
                break
            elif charToCapture == 'alpha':
                if not inp[index].isalpha():
                    groups.append(inp[start:index])
                    start = index
                    charToCapture = None
                    continue  # Do not bump index value
                else:
                    pass
            else:
                if inp[index] != ']':
                    if (inp[index] == '['):
                        bracketCount += 1
                else:
                    bracketCount -= 1
                    if (bracketCount == 0):
                        groups.append(inp[start:index + 1])
                        start = index + 1
                        charToCapture = None

        index = index + 1

    return groups


def multiply(group: str) -> str:
    if group.isalpha():
        return group
    else:
        multiplier = int(group[0])
        return ''.join([
            match * multiplier if match.isalpha()
            else processGroup(match) * multiplier
            for match in re.findall('\\d\\[(.+)\\]', group)
        ])


def processGroup(group: str) -> str:
    groups = splitGroups(group)
    return ''.join(map(multiply, groups))


print(processGroup(input()))
