n = list(map(int, input().split()))
a = max(n)
b = min(n)
a2 = min(n)
b2 = max(n)
for i in range(len(n)):
    if n[i] == a:
        a0 = i
    if n[i] == b:
        b0 = i
for i in range(len(n)):
    if n[i] > b and n[i] <= a and i != a0:
        a4 = i
    if n[i] >= b and n[i] < a and i != b0:
        b4 = i
a1 = min(n)
b1 = max(n)
for i in range(len(n)):
    if n[i] > a1 and n[i] <= n[a0] and i != a0 and i != a4:
        a1 = n[i]
        a2 = a1 * a * n[a4]
        a3 = i
    if n[i] >= n[b0] and n[i] < b1 and i != b0 and i != b4:
        b1 = n[i]
        b2 = b1 * b * n[b4]
        b3 = i
print(b1)
if a2 >= b2:
    print(a, n[a4], a1)
else:
    print(b1, n[b4], b)
