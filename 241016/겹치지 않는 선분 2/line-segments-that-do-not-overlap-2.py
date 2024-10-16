N = int(input())

arr = []

for _ in range(N):
    arr.append(tuple(map(int,input().split())))
arr2 = [0] * N

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if (arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]) or (arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]):
            arr2[i] += 1
            arr2[j] += 1

cnt = 0

for i in range(len(arr2)):
    if arr2[i] == 0:
        cnt += 1

print(cnt)