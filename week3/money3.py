import math
p = float(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
x = x * 100 + y
while i <= k:
    x = math.floor(x + x * (p / 100))
    i += 1
y = str(int((x) % 100) // 10) + str(int((x) % 10))
print(int(x // 100), y)
