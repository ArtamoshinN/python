s = str(input())
i = s.find('h')
j = i
while s.find('h', j) != -1:
    j = s.find('h', j) + 1
s1 = s[i + 1:j - 1]
s1 = s1.replace('h', 'H')
print(s[:i + 1] + s1.replace('h', 'H') + s[j - 1:])
