import math
x = int(input())
i = 0
kv = 0
sum = 0
while x != 0:
    kv = kv + x ** 2
    sum = sum + x
    x = int(input())
    i += 1
s = float(sum / i)
sigma = float(math.sqrt((kv - 2 * s * sum + i * s ** 2) / (i - 1)))
print('{0:.11f}'.format(sigma))
