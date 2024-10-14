string = list(input())

num = 0

for i in range(len(string)):
    if string[i] == '(':
        num += 1
    else:
        num -= 1
    if num < 0:
        print('No')
        break
    if i == len(string) -1 and num == 0:
        print('Yes')
    elif i == len(string) -1 and num != 0:
        print('No')