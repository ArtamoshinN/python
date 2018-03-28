n = open('input.txt', 'r', encoding='utf8')
m = open('output.txt', 'w', encoding='utf8')
k = list(n.readlines())
n = len(k)
p = []


class Student:
    sname = ''
    name = ''
    nc = 0
    b = 0
for i in range(n):
    l = list(k[i].split())
    l.remove(l[-2])
    sname, name, b = l
    b = int(b)
    st = Student()
    st.sname = sname
    st.name = name
    st.b = b
    p.append(st)


def name(st):
    return (st.sname, st.name, st.b, st.nc)
p.sort(key=name)
for now in p:
    print(now.sname, now.name, now.b, file=m)
m.close()
