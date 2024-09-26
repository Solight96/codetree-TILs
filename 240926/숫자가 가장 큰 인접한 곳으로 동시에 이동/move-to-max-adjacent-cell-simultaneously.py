import copy

n,m,t = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]
cnt = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    cnt[r][c] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0<= y and y < n

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(t):
    nextcnt = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if cnt[x][y] == 1:
                val, loc = -1, (-1,-1)
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        if val < v[nx][ny]:
                            val, loc = v[nx][ny], (nx, ny)
                nextcnt[loc[0]][loc[1]] += 1

    cnt = copy.deepcopy(nextcnt)

    for i in range(n):
        for j in range(n):
            if cnt[i][j] >= 2:
                cnt[i][j] = 0

result = 0

for i in range(n):
    for j in range(n):
        if cnt[i][j] == 1:
            result += 1

print(result)