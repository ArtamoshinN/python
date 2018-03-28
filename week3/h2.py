s = str(input())
p1 = s.find('h')
p2 = p1
while s.find('h', p2) != -1:
    p2 = s.find('h', p2) + 1
p2 = p2 - 1
print(s[:p2] + s[p1 + 1:p2] + s[p2:])
