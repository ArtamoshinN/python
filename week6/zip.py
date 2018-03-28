n = list(map(int, input().split()))
c = []
k = 0
for i in range(n[1]):
    a = int(input())
    c.append(a)
for i in range(n[1]):
    a = min(c)
    c.remove(a)
    if n[0] - a >= 0:
        n[0] = n[0] - a
        k += 1
print(k)
