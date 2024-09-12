N, M = map(int, input().split())

v = [[0] * N for _ in range(N)]

def in_range(x, y):
    return 0<=x and x<N and 0<=y and y<N

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


for _ in range(M):
    r, c = map(int, input().split())
    cnt = 0
    v[r-1][c-1] = 1
    for dx, dy in zip(dxs, dys):
        nr, nc = r+dx, c+dy
        if in_range(nr-1, nc-1) and v[nr-1][nc-1] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)