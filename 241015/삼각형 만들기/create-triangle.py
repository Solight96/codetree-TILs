N = int(input())

arr = []

for _ in range(N):
    arr.append(tuple(map(int, input().split())))

result = 0

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        num = 0
        if arr[i][0] == arr[j][0]:
            for k in range(j+1, len(arr)):
                if arr[i][1] == arr[k][1] or arr[j][1] == arr[k][1]:
                    num = abs(arr[i][1]-arr[j][1]) * abs(arr[j][0]-arr[k][0])
                    result = max(result, num)
        elif arr[i][1] == arr[j][1]:
            for k in range(j+1, len(arr)):
                if arr[i][0] == arr[k][0] or arr[j][0] == arr[k][0]:
                    num = abs(arr[i][0]-arr[j][0]) * abs(arr[j][1]-arr[k][1])
                    result = max(result, num)
        else:
            for k in range(j+1, len(arr)):
                if arr[i][0] == arr[k][0] and arr[j][1] == arr[k][1]:
                    num = abs(arr[i][1]-arr[k][1]) * abs(arr[j][0]-arr[k][0])
                    result = max(result, num)
                elif arr[i][1] == arr[k][1] and arr[j][0] == arr[k][0]:
                    num = abs(arr[i][0]-arr[k][0]) * abs(arr[j][1]-arr[k][1])
                    result = max(result, num)

print(result)