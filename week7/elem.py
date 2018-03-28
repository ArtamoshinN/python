a = map(int, input().split())
s = set()
for elem in a:
    if elem in s:
        print('YES')
    else:
        print('NO')
        s.add(elem)
