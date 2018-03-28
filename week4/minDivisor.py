def MinDivisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            break
        elif i >= n ** 0.5:
            return n
            break
        else:
            i += 1
    return i
n = int(input())
print(MinDivisor(n))
