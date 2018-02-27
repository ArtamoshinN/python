n = int(input())
a = n // 1000 - n % 10
b = n // 100 % 10 - n // 10 % 10
print(2 ** (-1 *  (a + b)))
