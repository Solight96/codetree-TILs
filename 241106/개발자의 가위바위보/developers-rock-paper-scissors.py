N = int(input())

arr = []

for _ in range(N):
    arr.append(tuple(map(int, input().split())))

arr2 = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
result = []

for i in range(len(arr2)):
    pri = arr2[i]
    cnt = 0
    for j in range(len(arr)):
        a, b = arr[j]
        if pri.index(a) < pri.index(b) and not (a == pri[1] and b == pri[-1]):
            cnt += 1
    result.append(cnt)

print(max(result))