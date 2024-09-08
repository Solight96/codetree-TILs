n, t = map(int, input().split())
num = list(map(int, input().split()))

cnt = 1
result = 0

for i in range(len(num)):
    if i == 0 and num[0] <= t:
        cnt = 0
    else:
        if num[i] > t:
            if num[i-1] > t:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
    
    if result <= cnt:
        result = cnt

print(result)