from typing import List, Union
import re


def process_group(group: str) -> str:
    if group.isalpha():
        return group
    else:
        multiplier, match = re.findall('(\\d)\\[(.+)\\]', group)[0]
        return int(multiplier) * (
            match if match.isalpha() else split_string_to_groups(match)
        )


def split_string_to_groups(inp: str):
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
            if index == len(inp) - 1:
                # Last character in input
                groups.append(inp[start:index + 1])
                break
            elif charToCapture == 'alpha':
                if not inp[index].isalpha():
                    groups.append(inp[start:index])
                    start = index
                    charToCapture = None
                    continue  # Do not bump index value
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

    return ''.join(map(process_group, groups))


print(split_string_to_groups(input()))
