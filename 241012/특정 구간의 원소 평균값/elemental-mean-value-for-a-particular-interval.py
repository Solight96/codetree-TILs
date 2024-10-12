N = int(input())

arr = list(map(int, input().split()))

result = 0
cnt = 0

for i in range(N):
    for j in range(i, N):
        num = 0
        for k in range(i, j+1):
            num += arr[k]
        
        result = num / (j-i+1)
        
        if result in arr[i:j+1]:
            cnt += 1

print(cnt)