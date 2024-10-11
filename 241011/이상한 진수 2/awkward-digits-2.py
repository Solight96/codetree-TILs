a = list(input())

for i in range(len(a)):
    if i == len(a)-1 and a[i] == '1':
        a[i] = '0'

    elif a[i] == '0':
        a[i] = '1'
        break

num = 0

for i in range(len(a)):
    num = 2 * num + int(a[i])

print(num)