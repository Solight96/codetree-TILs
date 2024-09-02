n = int(input())
i = 0
chk = 0
a = n

while 1:
    i += 1
    a = a // i
    chk += 1

    if a <= 1:
        break

print(chk)