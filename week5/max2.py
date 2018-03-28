n = list(map(int, input().split()))
a = max(n)
b = min(n)
for i in range(len(n)):
    if n[i] == a:
        a0 = i
    if n[i] == b:
        b0 = i
a1 = b
b1 = a
for i in range(len(n)):
    if n[i] > a1 and n[i] <= n[a0] and i != a0:
        a1 = n[i]
        a2 = a1 * a
        a3 = i
    if n[i] >= n[b0] and n[i] < b1 and i != b0:
        b1 = n[i]
        b2 = b1 * b
        b3 = i
if a2 >= b2:
    print(a1, a)
else:
    print(b, b1)
