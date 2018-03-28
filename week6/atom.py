n = int(input())
m = list(map(int, input().split()))
a = int(input())
b = list(map(int, input().split()))
for j in range(len(m)):
    k = 100000
    for i in range(len(b)):
        if abs(b[i] - m[j]) < k:
            k = abs(b[i] - m[j])
            d = i + 1
    print(d, end=' ')
