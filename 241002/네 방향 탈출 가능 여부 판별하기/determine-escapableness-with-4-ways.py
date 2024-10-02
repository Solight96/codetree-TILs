from collections import deque

q = deque()

n, m = map(int,input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def is_snake(x,y):
    return board[x][y] == 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not is_snake(nx, ny) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))


visited[0][0] = 1
q.append((0,0))
bfs()

if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)