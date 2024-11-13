n = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    minimum = i
    for j in range(i+1, len(arr)):
        if arr[minimum] > arr[j]:
            minimum = j
    tmp = arr[minimum]
    arr[minimum] = arr[i]
    arr[i] = tmp

print(*arr)