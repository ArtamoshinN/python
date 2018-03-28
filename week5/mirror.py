a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 10 == i // 1000:
        if i // 100 % 10 == i // 10 % 10:
            print(i)
