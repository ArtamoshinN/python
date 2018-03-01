y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
if ((y2 + x2) % 2 == 0) and ((y1 + x1) % 2 == 0):
    if (y2 >= y1):
        if ((y2 - y1) >= (x1 - x2)) and ((y2 - y1) >= (x2 - x1)):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
