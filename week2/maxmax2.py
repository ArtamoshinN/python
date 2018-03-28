a = -1
b = 0
m = 0
n = int(input())
while n != 0:
    if a == n:
        b += 1
    else:
        a = n
        m = max(m, b)
        b = 1
    n = int(input())
m = max(m, b)
print(m)
