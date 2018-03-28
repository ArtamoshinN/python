def IsAscending(A):
    i = 0
    while i + 1 < len(A) and A[i] < A[i + 1]:
        i += 1
    if (i + 1) == len(A):
        return 'YES'
    else:
        return'NO'
A = list(map(int, input().split()))
print(IsAscending(A))
