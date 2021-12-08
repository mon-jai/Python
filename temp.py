from typing import List


def insertion_sort(arr: List[int]):
    result = [arr[0]]
    for i in arr[1:]:
        for index, j in enumerate(result):
            if i > j:
                result = result[0:index] + [j] + result[index:]
                break
    return result
