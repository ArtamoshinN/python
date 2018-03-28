a = open('input.txt')
myDict = dict()
for line in a:
    newLine = line.split()
    for word in newLine:
        if word not in myDict:
            myDict[word] = 0
        else:
            myDict[word] += 1
        print(myDict[word], end=' ')
