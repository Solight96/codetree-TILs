string = str(input())
arr = list(string)

for i in range(len(arr)):
    if arr[i] == 'e':
        arr.pop(i)
        break

result = ''.join(arr)

print(result)