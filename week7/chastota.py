a = open('input.txt')
newLine = []
words = dict()
newWord = []
q = 0
for line in a:
    newLine += line.split()
for elem in newLine:
    if elem not in words:
        words[elem] = 0
    words[elem] += 1
for elem in words:
    newWord.append((words[elem], elem))
newWord.sort(key=lambda x: (-x[0], x[1]))
for elem in newWord:
    print(elem[1])
