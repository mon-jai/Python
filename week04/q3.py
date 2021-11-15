def forOps():
    myString = "ATCgATAgcTCGaTCG"
    count = 0
    for index in myString:
        if index.isupper():
            count+=1
    return count

print(forOps())