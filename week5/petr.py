n = list(map(int, input().split()))
m = int(input())
k = 0
for i in range(len(n)):
    if m <= n[i]:
        k += 1
print(k + 1)
