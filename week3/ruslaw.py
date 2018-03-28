import math
x = float(input())
if x * 10 % 10 >= 5:
    print(math.ceil(x))
else:
    print(math.floor(x))
