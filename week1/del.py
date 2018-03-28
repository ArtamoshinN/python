a = int(input())
b = int(input())
c = a % b == 0
print('YES' * c, 'NO' * (1 - c), sep='')
