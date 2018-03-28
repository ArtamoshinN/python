inp = open('input.txt', 'r', encoding='utf8')
out = open('output.txt', 'w', encoding='utf8')
k = int(inp.readline())
p = []
for i in inp:
    n = i.split()
    if int(n[-1]) >= 40 and int(n[-2]) >= 40 \
            and int(n[-3]) >= 40:
        p.append(n)
p.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
p.reverse()
t = []
for i in p:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    t.append(sum)
m = len(t)


def kto(m, k, t):
    if m <= k:
        return 0
    elif t.count(max(t)) > k:
        return 1
    for i in range(k, 0, -1):
        if t[i] < t[i - 1]:
            return t[i - 1]


print(kto(m, k, t))
