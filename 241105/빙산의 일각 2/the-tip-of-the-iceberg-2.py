import copy

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

result = []

for h in range(max(arr)):
    arr2 = copy.deepcopy(arr)
    for i in range(len(arr2)):
        if arr2[i] <= h:
            arr2[i] = 0
    
    cnt = 0

    for i in range(len(arr2)-1):
        if arr2[i] != 0 and arr2[i+1] == 0:
            cnt += 1
    
    if arr2[-1] != 0 :
        result.append(cnt+1)
    else:
        result.append(cnt)

print(max(result))