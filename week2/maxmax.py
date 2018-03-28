n1 = int(input())
i = 1
j = 0
while n1 != 0:
    n2 = int(input())
    if n1 == n2:
        i += 1
    elif i >= j:
        j = i
        i = 1
    n1 = n2
print(j)
