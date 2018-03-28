n = int(input())
i = 2
sum = 1
while i <= n:
    sum += 1 / (i ** 2)
    i += 1
print('{0:.6f}'.format(sum))
