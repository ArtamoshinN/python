a = open('input.txt', 'r', encoding='utf8')
b = open('output.txt', 'w', encoding='utf8')
newLine = []
newName = []
golos = dict()
i = 0
for line in a:
    newLine.append(line.strip())
for name in newLine:
    if name not in golos:
        golos[name] = 0
    golos[name] += 1
    i += 1
i = i / 2
for name in golos:
    newName.append((name, golos[name]))
    newName.sort(key=lambda x: -x[1])
for name in newName:
    if name[1] > i:
        print(name[0], file=b)
        break
    else:
        for i in range(2):
            print(newName[i][0], file=b)
        break
b.close()
