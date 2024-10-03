from collections import deque

n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque()

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def is_wall(x,y):
    return board[x][y] == 1

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

cnt = 0

def bfs(x,y):
    global cnt 
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not is_wall(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

for _ in range(k):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1
    q.append((r,c))
    bfs(r, c)

print(cnt)