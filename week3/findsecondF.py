s = str(input())
i = s.find('f')
if i == -1:
    print(-2)
else:
    s = s[:i] + s[i + 1:]
    j = s.find('f')
    if j == -1:
        print(-1)
    else:
        print(j + 1)
