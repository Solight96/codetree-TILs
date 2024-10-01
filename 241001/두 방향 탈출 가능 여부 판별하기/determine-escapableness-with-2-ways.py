n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def is_snake(x, y):
    return board[x][y] == 0

dxs = [0, 1]
dys = [1, 0]

def dfs(x, y):
    for dx,dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and not is_snake(nx, ny):
            x2, y2 = nx, ny
            visited[x2][y2] = True
            dfs(x2, y2)

visited[0][0] = True
dfs(0, 0)

if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)