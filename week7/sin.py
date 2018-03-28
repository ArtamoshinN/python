n = int(input())
k = {}
for i in range(n):
    a = input()
    s1, s2 = a.split()
    k[s1] = []
    k[s1].append(s2)
word = input()
for elem in k:
    if [word] == k[elem]:
        print(elem)
    elif word == elem:
        print(*k[elem])
