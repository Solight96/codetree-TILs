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

    arr = []

    for _ in range(M):
        x, y, d = input().split()
        x, y = int(x)-1, int(y)-1
        v[x][y] = 1 # 1은 폭탄
        if d == 'U': d = 0
        elif d == 'R': d = 1
        elif d == 'D': d = 2
        elif d == 'L': d = 3

        arr.append([x,y,d])    
    
    for _ in range(2*N):
        cnt = [[0] * N for _ in range(N)]
        arr_result = []

        for i in range(len(arr)):
            nx, ny = arr[i][0] + dxs[arr[i][2]%4], arr[i][1] + dys[arr[i][2]%4]
            if in_range(nx, ny):
                arr[i] = [nx,ny,arr[i][2]]
            else:
                arr[i] = [arr[i][0],arr[i][1],arr[i][2]+2]
                
        for i in range(len(arr)):
            cnt[arr[i][0]][arr[i][1]] += 1
        for i in range(len(arr)):
            if cnt[arr[i][0]][arr[i][1]] == 1:
                arr_result.append(arr[i])
        
        arr = copy.deepcopy(arr_result)
        
    print(len(arr))