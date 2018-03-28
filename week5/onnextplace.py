n = list(map(int, input().split()))
a = n.copy()
a[0] = n[-1]
for i in range(len(n) - 1):
    a[i + 1] = n[i]
print(*a)
