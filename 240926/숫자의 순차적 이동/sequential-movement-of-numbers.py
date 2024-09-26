import copy

n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]
v2 = copy.deepcopy(v)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [-1,0,1,0,-1,1,1,-1]
dys = [0,1,0,-1,1,1,-1,-1]

for _ in range(m):
    for num in range(1, n**2 +1):
        for x in range(n):
            for y in range(n):
                if v[x][y] == num:
                    val, loc = -1, (-1, -1)
                    for dx, dy in zip(dxs,dys):
                        nx, ny = x+dx, y+dy
                        if in_range(nx, ny) and val < v2[nx][ny]:
                            val, loc = v2[nx][ny], (nx, ny)
                    v2[loc[0]][loc[1]] = num
                    v2[x][y] = val
        
        v = copy.deepcopy(v2)

for elem in v:
    print(*elem)