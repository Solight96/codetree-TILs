arr = []

for _ in range(2):
    string = str(input())
    for i in range(len(string)):
        if string[i] != ' ':
            arr.append(string[i])

for i in range(len(arr)):
    print(arr[i], end='')