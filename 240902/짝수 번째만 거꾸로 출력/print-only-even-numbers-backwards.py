string = str(input())
arr = []

for i in range(len(string)):
    if i%2 != 0:
        arr.append(string[i])

arr.reverse()

for i in range(len(arr)):
    print(arr[i], end='')