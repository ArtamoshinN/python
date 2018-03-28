a = int(input())
b = int(input())
if a > b:
    k = -1
else:
    k = 1
for i in range(a, b + k, k):
    print(i, end=' ')
