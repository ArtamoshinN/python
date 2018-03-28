n = open('input.txt', 'r', encoding='utf8')
p = set()
for i in n:
    i = i.split()
    i = set(i)
    p = p | i
print(len(p))
