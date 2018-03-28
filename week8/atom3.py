n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in range(m):
    b[i] = [i + 1, b[i]]
for i in range(n):
    a[i] = [i + 1, a[i]]
b.sort(key=lambda x: x[1])
j = 0
for elem in a:
    if elem[1] < b[0][1]:
        elem = [b[0][0], elem[1]]
    if elem[1] > b[-1][1]:
        elem = [b[-1][0], elem[1]]
        m -= 1
    while elem[1] > b[j][1] and j < m:
        if abs(b[j][1] - elem[1]) >= abs(b[j + 1][1] - elem[1]):
            elem = [b[j + 1][0], elem[1]]
            j += 1
        else:
            elem = [b[j][0], elem[1]]
            j += 1
    j = 0
    print(elem[0], end=' ')
