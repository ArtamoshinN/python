def IsPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return 'NO'
            break
        elif i >= n ** 0.5:
            return 'YES'
            break
        else:
            i += 1
    return 'YES'
n = int(input())
print(IsPrime(n))
