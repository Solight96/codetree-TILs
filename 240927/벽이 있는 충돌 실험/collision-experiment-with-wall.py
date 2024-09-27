import copy

T = int(input())

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

for _ in range(T):
    N, M = map(int,input().split())

    def in_range(x, y):
        return 0 <= x and x < N and 0 <= y and y < N

    v = [[0] * N for _ in range(N)]
    direct = [[-1] * N for _ in range(N)]

    for _ in range(M):
        x, y, d = input().split()
        x, y = int(x)-1, int(y)-1
        v[x][y] = 1 # 1은 폭탄
        if d == 'U': direct[x][y] = 0
        elif d == 'R': direct[x][y] = 1
        elif d == 'D': direct[x][y] = 2
        elif d == 'L': direct[x][y] = 3    
    
    for _ in range(2*N):
        v2 = [[0] * N for _ in range(N)]
        direct2 = [[-1] * N for _ in range(N)]

        for x in range(N):
            for y in range(N):
                if v[x][y] == 1:
                    nx, ny = x + dxs[direct[x][y]%4], y + dys[direct[x][y]%4]
                    if in_range(nx, ny):
                        v2[nx][ny] += 1
                        direct2[nx][ny] = direct[x][y]
                    else:
                        v2[x][y] += 1
                        direct2[x][y] = direct[x][y] + 2
                
        for x in range(N):
            for y in range(N):
                if v2[x][y] >= 2:
                    v2[x][y] = 0
                    direct2[x][y] = -1
                
        v = copy.deepcopy(v2)
        direct = copy.deepcopy(direct2)
    
    cnt = 0

    for i in range(N):
        for j in range(N):
            if v[i][j] == 1:
                cnt += 1
        
    print(cnt)