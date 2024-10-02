n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [0,-1,0,1,0]
dys = [0,0,1,0,-1]

cnt = 0

def dfs(x, y, i):
    global cnt
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and visited[nx][ny] == 0 and board[nx][ny] == i:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny, i)

arr = []

for i in range(n):
    for j in range(n):
        dfs(i,j,board[i][j])
        if cnt != 0:
            arr.append((board[i][j], cnt))
        cnt = 0

num_block = 0
size_block = 0

for i in range(len(arr)):
    if arr[i][1] >= 4:
        num_block += 1
    if arr[i][1] > size_block:
        size_block = arr[i][1]

print(num_block, size_block)