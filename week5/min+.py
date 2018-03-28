n = list(map(int, input().split()))
k = 0
j = max(n)
for i in range(len(n)):
    if n[i] > 0 and n[i] <= j:
        j = n[i]
print(j)
