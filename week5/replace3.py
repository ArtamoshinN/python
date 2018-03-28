n = list(map(int, input().split()))
for i in range(len(n) // 2):
    n[i * 2], n[i * 2 + 1] = n[i * 2 + 1], n[i * 2]
print(*n)
