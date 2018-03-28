s = str(input())
if s.find('h') != -1:
    f = s.find('h')
    s1 = s[f + 1:]
    if s1.find('h') != -1:
        s2 = s[::-1]
        if s2.find('h') != -1 * f - 1 and s2.find('h') != -1:
            f = s2.find('h')
            k = len(s2) - f - 1
st = s[:f - 1] + s[k + 1:]
print(st)
