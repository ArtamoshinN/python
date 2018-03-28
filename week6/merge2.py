import heapq


def merge(a, b):
    c = heapq.merge(a, b)
    return c
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
