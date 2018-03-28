import math
a = float(input())
b = float(input())
c = float(input())
if b ** 2 - 4 * a * c > 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x1 == 0 or x2 == 0:
        print(3)
    elif x1 > x2:
        print(2, '{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
    else:
        print(2, '{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
elif b ** 2 - 4 * a * c == 0:
    x = -b / (2 * a)
    print(1, '{0:.6f}'.format(x))
elif b ** 2 - 4 * a * c < 0:
    print(0)
else:
    print(3)
