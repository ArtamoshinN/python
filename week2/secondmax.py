n = int(input())
n1 = 0
n2 = 0
while n != 0:
    if n >= n1:
        n2 = n1
        n1 = n
    elif n >= n2:
        n2 = n
    n = int(input())
print(n2)
