n = int(input())
r = list(map(int, input().split()))
r = sorted(r)
t = []
for i in range(len(r)):
    if r[i] >= n:
        t.append(r[i])
if len(t) >= 1:
    k = 1
    for i in range(len(t) - 1):
        if t[i + 1] - t[i] >= 3:
            k += 1
print(k)
