a = int(input())
b = int(input())
n1 = abs(a - b)
m1 = abs(a + b)
n2 = abs(b - a)
m2 = abs(a + b)
print((n1 + m1 + n2 + m2) // 4)
