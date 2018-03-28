k = int(input())
n = list(map(int, input().split()))
b = int(input())
j = 0
c = 2001
if k == len(n):
    for i in range(k):
        if abs(n[i] - b) < c:
            c = abs(n[i] - b)
            j = n[i]
print(j)
