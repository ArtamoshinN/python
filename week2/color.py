y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
if ((y1 - y2) % 2 == 1) and ((x1 - x2) % 2 == 1):
    print('YES')
elif ((y1 - y2) % 2 == 0) and ((x1 - x2) % 2 == 0):
    print('YES')
else:
    print('NO')
