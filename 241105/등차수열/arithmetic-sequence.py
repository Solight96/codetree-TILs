n = int(input())

num = list(map(int, input().split()))

result = []

for k in range(min(num), max(num)+1):
    cnt = 0
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if k-num[i] == num[j]-k:
                cnt += 1
    
    result.append(cnt)

print(max(result))