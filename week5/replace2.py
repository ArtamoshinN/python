n = list(map(int, input().split()))
a = n[:]
for i in range(len(n)):
    a[i] = n[-1 - i]
n = a[:]
print(*n)
