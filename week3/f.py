s = str(input())
if s.find('f') != -1:
    f = s.find('f')
    print(f, end=' ')
    s1 = s[f + 1:]
    if s1.find('f') != -1:
        s2 = s[::-1]
        if s2.find('f') != -1 * f - 1 and s2.find('f') != -1:
            f = s2.find('f')
            f = len(s2) - f - 1
            print(f)
