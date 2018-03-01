y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
if (y1 - y2 == 1) or (y1 - y2 == -1) or (y1 - y2 == 0):
    if (x1 - x2 == 1) or (x1 - x2 == -1) or (x1 - x2 == 0):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
