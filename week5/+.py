n = list(map(int, input().split()))
k = 0
for i in range(len(n)):
    if n[i] > 0:
        k += 1
print(k)
