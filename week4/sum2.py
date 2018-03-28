def sum2(n):
    n = int(input())
    if n == 0:
        return n
    return n + sum2(n)
n = 0
print(sum2(n))
