n = list(map(int, input().split()))
k = 0
m = max(n)
for i in range(len(n)):
    if n[i] <= m and n[i] % 2 == 1:
        k = i
        m = n[i]
print(n[k])
