a = list(map(int, input().split()))
k = 0
for i in range(len(a) - 1):
    if a[i] > a[i + 1] and a[abs(i - 1)] < a[i] and i - 1 >= 0:
        k += 1
print(k)
