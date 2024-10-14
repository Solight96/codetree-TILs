string = list(input())

num = 0

for i in range(len(string)):
    if string[i] == '(':
        num += 1
    else:
        num -= 1

if string[0] == '(' and num == 0:
    print('Yes')
else:
    print('No')