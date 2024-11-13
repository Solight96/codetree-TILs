import sys

n = int(input())

arr = list(map(int, input().split()))


for i in range(len(arr)-1):
    minimum = sys.maxsize
    for j in range(i, len(arr)):
        if minimum > arr[j]:
            minimum = arr[j]
    
    idx = arr.index(minimum)
    tmp = arr[i]
    arr[i] = arr[idx]
    arr[idx] = tmp

print(*arr)