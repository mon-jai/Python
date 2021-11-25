from typing import List

def gen(n:int):
    d0 = [1 for _ in range(9)]
    data=[d0]
    for i in range(n):
        d=[1]
        for j in range(1,9):
            c = d[j-1]+data[i][j]
            d.append(c)
        data.append(d)
    return data

def countData(data: List[List[int]], index: int, start: int, end: int):
    count=0
    for i in range(start-1, end-1):
        count = count + data[index-1][8-i]
    return count

def compute(N: str):
    count=0
    length = len(N)
    data = gen(length)
    for i in range(1, length):
        count = count + sum(data[i-1])
    count = count + countData(data, length, 1, int(N[0]))
    for i in range(length-1,0,-1):
        if (int(N[length-i-1])>int(N[length-i])):
            break
        count = count + countData(data, i, int(N[length-i-1]), int(N[length-i]))
        if (i==1):
            count = count +1
    return count


print(compute(input()))