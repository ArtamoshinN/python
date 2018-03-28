n = list(map(int, input().split()))
k = 1
for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        k += 1
print(k)
