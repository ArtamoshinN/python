p = float(input())
x = int(input())
y = int(input())
p = (x * 100 + y + x * 100 * (p / 100) + y * (p / 100)) / 100
y = int(str(int((p * 100) % 100) // 10) + str(int((p * 100) % 10)))
print(int(p), y)
