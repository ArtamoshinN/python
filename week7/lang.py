n = int(input())
s1 = set()
s2 = set()
s3 = set()
if n != 0:
    k = int(input())
    if k != 0:
        for i in range(k):
            lan = input()
            s1.add(lan)
            s2.add(lan)
    if n - 1 != 0:
        for i in range(n - 1):
            k = int(input())
            if k != 0:
                for j in range(k):
                    lan = input()
                    s1.add(lan)
                    s3.add(lan)
            else:
                continue
            s2 &= s3
            s3.clear()
print(len(s2))
for lan in sorted(s2):
    print(lan)
print(len(s1))
for lan in sorted(s1):
    print(lan)
