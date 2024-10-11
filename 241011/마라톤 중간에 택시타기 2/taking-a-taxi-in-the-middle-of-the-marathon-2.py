import sys
import copy

N = int(input())

arr = []

for _ in range(N):
    cp = tuple(map(int, input().split()))
    arr.append(cp)

arr2 = copy.deepcopy(arr)
result = sys.maxsize

for i in range(1, len(arr)-1):
    distance = 0
    arr2.pop(i)

    for j in range(len(arr2)-1):
        distance += abs(arr2[j][0] - arr2[j+1][0]) + abs(arr2[j][1] - arr2[j+1][1])
    
    if distance < result:
        result = distance
    arr2 = copy.deepcopy(arr)

print(result)