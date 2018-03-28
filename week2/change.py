n = int(input())
i = 1
print(n % 10, end='')
while i < int(len(str(n))):
    print(n // (10 ** i) % 10, end='')
    i += 1
