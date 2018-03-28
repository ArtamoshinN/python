a = list(input())


def num(a):
    b = ['8', '4', '9', '5']
    if a.count('(') != 0:
        a.remove('(')
        a.remove(')')
    for i in range(a.count('-')):
        a.remove('-')
    if a[0] == '+':
        a.remove(a[1])
        a[0] = '8'
    if len(a) == 7:
        for i in range(len(a)):
            b.append(a[i])
        a = b
    return a
for i in range(3):
    b = list(input())
    if num(a) == num(b):
        print('YES')
    else:
        print('NO')
