n = list(map(int, input().split()))
k = int(input())
n.pop(k)
print(*n)
