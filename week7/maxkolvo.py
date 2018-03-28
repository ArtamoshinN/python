a = open('input.txt')
newLine = []
words = dict()
q = 0
for line in a:
    newLine += line.split()
for elem in newLine:
    if elem not in words:
        words[elem] = 0
    words[elem] += 1
for c in sorted(words):
    if words[c] > q:
        q = words[c]
        w = c
print(w)
