string = str(input())
arr = []

for i in range(len(string)):
    if ord(string[i])>=97:
        arr.append(chr(ord(string[i])-32))
    elif ord(string[i])>=65:
        arr.append(chr(ord(string[i])+32))

result = ''.join(arr)
print(result)