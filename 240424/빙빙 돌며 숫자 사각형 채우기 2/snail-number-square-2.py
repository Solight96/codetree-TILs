n, m = map(int, input().split())

v = [[0] * m for _ in range(n)]

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < m

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0

dir_num = 2

for i in range(1, n*m+1):
    v[x][y] = i
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if in_range(nx, ny) and v[nx][ny] == 0:
        x = x + dx[dir_num]
        y = y + dy[dir_num]
    else:
        dir_num = (dir_num+3)%4
        x = x + dx[dir_num]
        y = y + dy[dir_num]

for i in range(n):
    for j in range(m):
        print(v[i][j], end = ' ')
    print()