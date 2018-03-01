a = int(input())
b = int(input())
n1 = ((a - b) ** 2) ** 0.5
m1 = ((a + b) ** 2) ** 0.5
n2 = ((b - a) ** 2) ** 0.5
m2 = ((a + b) ** 2) ** 0.5
print((n1 + m1 + n2 + m2) // 4)
