import copy

N = int(input())

arr = []
# time = [0] * 1001

for _ in range(N):
    arr.append(tuple(map(int, input().split())))

result = 0

for i in range(len(arr)):
    arr2 = copy.deepcopy(arr)
    arr2.pop(i)
    time = [0] * 1001
    for j in range(len(arr2)):
        for k in range(arr2[j][0], arr2[j][1]):
            time[k] += 1
    
    cnt = 0

    for l in range(len(time)):
        if time[l] != 0:
            cnt += 1
    
    result = max(result, cnt)

print(result)