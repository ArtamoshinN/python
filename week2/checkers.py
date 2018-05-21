x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 <= 8 and x2 <= 8 and y1 <= 8 and y2 <= 8:
    if ((y2 + x2) % 2 == 0) and ((y1 + x1) % 2 == 0):
        if (y2 > y1):
            if ((y2 - y1) >= (x1 - x2)) and ((y2 - y1) >= (x2 - x1)):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
