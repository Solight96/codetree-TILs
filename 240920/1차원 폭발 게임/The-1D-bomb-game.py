N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

while True:
    temp = []
    index = []
    cnt = 1

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt += 1
            if i+1 == len(arr)-1 and cnt >= M:
                for j in range(i-cnt+2, i+2):
                    index.append(j)
        else:
            if cnt >= M:
                for j in range(i-cnt+1, i+1):
                    index.append(j)
            cnt = 1
    
    for i in range(len(arr)):
        if not i in index:
            temp.append(arr[i])
    if temp == arr:
        break
    arr = temp

print(len(arr))
    
for elem in arr:
    print(elem)