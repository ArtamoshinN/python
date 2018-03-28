n = list(map(int, input().split()))
m = 0
j = 0
for i in range(len(n)):
    if n[i] >= m:
        m = n[i]
        j = i
print(m, j)
