import copy
import sys

N = int(input())
arr = []

for _ in range(N):
    loc = tuple(map(int, input().split()))
    arr.append(loc)

result = sys.maxsize

for i in range(N):
    arr2 = copy.deepcopy(arr)
    arr2.pop(i)
    min_x, max_x, min_y, max_y = sys.maxsize, 0, sys.maxsize, 0
    for j in range(N-1):
        min_x = min(min_x, arr2[j][0])
        max_x = max(max_x, arr2[j][0])
        min_y = min(min_y, arr2[j][1])
        max_y = max(max_y, arr2[j][1])

    rec = (max_x - min_x) * (max_y - min_y)

    result = min(result, rec)

print(result)