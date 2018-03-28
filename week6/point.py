k = open('input.txt', 'r', encoding='utf8')
k = list(k.readlines())
n = len(k)


class Student:
    sname = ''
    name = ''
    nc = 0
    b = 0
c9 = 0
c10 = 0
c11 = 0
k9 = 0
k10 = 0
k11 = 0
for i in range(n):
    l = list(k[i].split())
    sname, name, nc, b = l
    nc = int(nc)
    b = int(b)
    st = Student()
    st.nc = nc
    st.b = b
    if st.nc == 9:
        c9 += st.b
        k9 += 1
    elif st.nc == 10:
        c10 += st.b
        k10 += 1
    elif st.nc == 11:
        c11 += st.b
        k11 += 1
print(c9 / k9, c10 / k10, c11 / k11)
