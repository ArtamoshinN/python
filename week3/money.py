import math
x = float(input())
y = int(round(x * 100) % 100)
print(math.floor(x), str(y // 10) + str(y % 10))
