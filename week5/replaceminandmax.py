n = list(map(int, input().split()))
m1 = min(n)
m2 = max(n)
for i in range(len(n)):
    if m1 == n[i]:
        a = i
    if m2 == n[i]:
        b = i
c = n[a]
n[a] = n[b]
n[b] = c
print(*n)
