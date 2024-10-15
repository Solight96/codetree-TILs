import sys

n = int(input())

arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

result = sys.maxsize

for i in range(len(arr)-1):
    dist = 0
    for j in range(i+1, len(arr)):
        dist = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
        result = min(result, dist)

print(result)