N = int(input())
arr= []

for _ in range(N):
    n = int(input())
    arr.append(n)

result = 0

for i in range(len(arr)):
    if i == 0:
        cnt = 1
    else:
        if arr[i-1] > 0 and arr[i] > 0:
            cnt += 1
            if result <= cnt:
                result = cnt
        elif arr[i-1] < 0 and arr[i] < 0:
            cnt += 1
            if result <= cnt:
                result = cnt
        else:
            cnt = 1

print(result)