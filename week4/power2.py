def power2(a, n):
    if n % 2 == 0:
        if n == 0:
            return 1
        return power2(a ** 2, n / 2)
    elif n % 2 == 1:
        if n == 0:
            return 1
        return a * power2(a, n - 1)
a = float(input())
n = int(input())
print(power2(a, n))
