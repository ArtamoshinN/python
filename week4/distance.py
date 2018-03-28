def distance(x1, y1, x2, y2):
    x1 = (x2 - x1) ** 2
    y1 = (y2 - y1) ** 2
    return (x1 + y1) ** 0.5
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print('{0:.6}'.format(distance(x1, y1, x2, y2)))
