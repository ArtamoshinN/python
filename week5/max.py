n = list(map(int, input().split()))
k = 0
m = min(n)
for i in range(len(n)):
    if n[i] > m:
        k = i
        m = n[i]
print(m, k)
