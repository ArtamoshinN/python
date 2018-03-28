n = list(map(int, input().split()))
k = list(map(int, input().split()))
c = k[1]
k = k[0]
n.insert(k, c)
print(*n)
