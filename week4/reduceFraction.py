def ReduceFraction(n, m):
    if m == 0:
        return n
    else:
        return ReduceFraction(m, n % m)
n = int(input())
m = int(input())
p = n
q = m
print(n // ReduceFraction(n, m), m // ReduceFraction(n, m))
