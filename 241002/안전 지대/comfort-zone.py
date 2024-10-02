import sys
sys.setrecursionlimit(3000)

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def is_water(x, y):
    return board_height[x][y] == 0

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not is_water(nx, ny) and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

max_region = 0
max_k = 1

for K in range(1, max(map(max, board))+1):
    board_height = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    region = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] > K:
                board_height[i][j] = 1

    for i in range(N):
        for j in range(M):
            if board_height[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j)
                region += 1
    
    if region > max_region:
        max_region = region
        max_k = K

print(max_k, max_region)