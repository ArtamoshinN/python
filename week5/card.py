n = int(input())
k = 0
for i in range(n):
    k = k + (i + 1)
for i in range(n - 1):
    n = int(input())
    k = k - n
print(k)
