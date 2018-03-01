n = int(input())
mm = str((n // 60 % 60) // 10) + str((n // 60 % 60) % 10)
ss = str((n % 60) // 10) + str((n % 60) % 10)
print((n // 60 // 60) % 24, ':', mm, ':', ss, sep='')
