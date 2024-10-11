import sys

N, S = map(int, input().split())

arr = list(map(int, input().split()))

result = sys.maxsize

for i in range(len(arr)-1):
    arr[i], arr[i+1] = 0, 0
    dist = abs(S - sum(arr))
    if result > dist:
        result = dist

print(result)