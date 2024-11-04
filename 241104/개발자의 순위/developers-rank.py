K, N = map(int, input().split())

arr = []

for _ in range(K):
    arr.append(input().split())

result = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        cnt = 0

        if i==j:
            continue
        else:
            for k in range(K):
                dev = arr[k]
                x = dev.index(str(i))
                y = dev.index(str(j))
                if x < y:
                    cnt += 1
            
            if cnt == K:
                result += 1
                
print(result)