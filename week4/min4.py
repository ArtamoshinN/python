def min4(a, b, c, d):
    a = min(a, b)
    a = min(a, c)
    a = min(a, d)
    return a
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
