length = int(input())
string = list(input())

num = 0

for i in range(length):
    if string[i] == 'C':
        for j in range(i+1, length):
            if string[j] == 'O':
                for k in range(j+1, length):
                    if string[k] == 'W':
                        num += 1
print(num)