n = int(input())
p = []
for i in range(n):
    k = list(input().split())
    k[1] = int(k[1])
    p.append(k)


def s(p):
    return (-p[1], p[0])
p.sort(key=s)
for i in range(n):
    print(p[i][0])
