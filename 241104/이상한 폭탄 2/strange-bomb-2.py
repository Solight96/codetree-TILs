N, K = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

result = -1

for i in range(1, max(arr)+1):
    if i in arr:
        idx = arr.index(i)
        for j in range(idx+1, idx+(K+1)):
            if j < len(arr) and arr[j] == i:
                result = i
                break

print(result)