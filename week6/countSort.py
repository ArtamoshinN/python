n = list(map(int, input().split()))
o = [0] * 101


def CountSort(n):
    for now in n:
        o[now] += 1
    for nowo in range(len(o)):
        print((str(nowo) + ' ') * o[nowo], end='')
CountSort(n)
