n = int(input())
if (n % 10 == 1) and (n != 11):
    print(n, 'korova')
elif (n > 21) or (n < 5):
    if (n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4):
        print(n, 'korovy')
    else:
        print(n, 'korov')
else:
    print(n, 'korov')