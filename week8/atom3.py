n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in range(m):
    b[i] = [i + 1, b[i]]
b.sort(key=lambda x: x[1])
m -= 1


def search(b, elem):
    k = int((len(b) - 1) / 2)
    i = k
    if elem <= b[0][1]:
        return b[0][0]
    elif elem >= b[len(b) - 1][1]:
        return b[len(b) - 1][0]
    while not (b[k][1] <= elem <= b[k + 1][1]):
        if elem < b[k][1]:
            k = k - int(i / 2)
            i /= 2
        elif elem > b[k][1]:
            k = k + int(i / 2)
            i /= 2
        else:
            return b[k][0]
    if elem != b[k][1]:
        if abs(b[k][1] - elem) < abs(b[k + 1][1] - elem):
            return b[k][0]
        else:
            return b[k + 1][0]
    else:
        return b[k][0]
for elem in a:
    print(*[search(b, elem)], end=' ')
