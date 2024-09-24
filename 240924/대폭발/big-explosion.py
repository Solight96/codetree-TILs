import copy

n,m,r,c = map(int, input().split())
r, c = r-1, c-1

v = [[0] * n for _ in range(n)]
v2 = [[0] * n for _ in range(n)]

v[r][c] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [0, -1, 0, 1, 0]
dys = [0, 0, 1, 0, -1]

for t in range(1, m+1):
    for x in range(n):
        for y in range(n):
            if v[x][y] == 1:
                for dx, dy in zip(dxs, dys):
                    nr, nc = x+dx*(2**(t-1)), y+dy*(2**(t-1))
                    if in_range(nr, nc):
                        v2[nr][nc] = 1
    
    v = copy.deepcopy(v2)

cnt = 0

for i in range(n):
    for j in range(n):
        if v[i][j] == 1:
            cnt += 1 

print(cnt)