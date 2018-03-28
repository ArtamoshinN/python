def merge(a, b):
    d = a + b
    c = []
    for i in range(len(a) + len(b)):
        m = min(d)
        c.append(m)
        d.remove(m)
    return c
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
