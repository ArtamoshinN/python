n = int(input())
max = 0
while n != 0:
    if max <= n:
        if max == n:
            i += 1
        else:
            i = 1
            max = n
    n = int(input())
if max == 0:
    i = 0
print(i)
