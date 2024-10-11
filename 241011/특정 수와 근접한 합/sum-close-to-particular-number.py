import sys
import copy

N, S = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = copy.deepcopy(arr)

result = sys.maxsize

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        arr2[i], arr2[j] = 0, 0
        dist = abs(S - sum(arr2))
        if result > dist:
            result = dist
        arr2 = copy.deepcopy(arr)

print(result)