a = int(input())
b = int(input())
c = int(input())
if c >= a and c >= b and a + b > c:
    if c ** 2 == a ** 2 + b ** 2:
        print('rectangular')
    elif c ** 2 > a ** 2 + b ** 2:
        print('obtuse')
    elif c ** 2 < a ** 2 + b ** 2:
        print('acute')
elif a >= c and a >= b and c + b > a:
    if a ** 2 == b ** 2 + c ** 2:
        print('rectangular')
    elif a ** 2 > b ** 2 + c ** 2:
        print('obtuse')
    elif a ** 2 < b ** 2 + c ** 2:
        print('acute')
elif b >= c and b >= a and a + c > b:
    if b ** 2 == a ** 2 + c ** 2:
        print('rectangular')
    elif b ** 2 > a ** 2 + c ** 2:
        print('obtuse')
    elif b ** 2 < a ** 2 + c ** 2:
        print('acute')
else:
    print('impossible')
