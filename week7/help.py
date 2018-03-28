m = int(input())
s = set(range(1, m + 1))
a = 0
y = 'YES'
n = 'NO'
while a != ['HELP']:
    a = input().split()
    if a == ['HELP']:
        continue
    else:
        b = str(input())
        a = list(map(int, a))
        a = set(a)
        if b == str(y):
            s &= a
        elif b == n:
            s -= a
print(*sorted(list(s)))
