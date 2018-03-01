n = int(input())
m = int(input())
k = int(input())
if (m <= k) and (k % m == 0) and (m * n > k):
    print('YES')
elif (n <= k) and (k % n == 0) and (m * n > k):
    print('YES')
else:
    print('NO')
