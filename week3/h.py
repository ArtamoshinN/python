s = str(input())
p1 = s.find('h')
p2 = p1
while s.find('h', p2) != -1:
    p2 = s.find('h', p2) + 1
p2 = p2 - 1
print(s[:p1] + s[p2 + 1:])
