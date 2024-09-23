n, m, k = map(int,input().split())

v = [list(map(int,input().split())) for _ in range(n)]

for j in range(k-1,k+m-1):
        v[0][j] = 1

for i in range(1, n):
    cnt = 0
    for j in range(k-1,k+m-1):
        if v[i][j] == 1:
            cnt += 1
    
    if cnt == 0:
        for j in range(k-1,k+m-1):
            v[i][j] = 1
            v[i-1][j] = 0
    else:
        break

for elem in v:
    print(*elem)