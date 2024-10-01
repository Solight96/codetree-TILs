n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def is_wall(x, y):
    return board[x][y] == 0

dxs = [0, 1]
dys = [1, 0]

arr = []

def dfs(x, y):
    visited[x][y] = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not is_wall(nx, ny) and not visited[nx][ny]:
            x2, y2 = nx, ny
            arr.append((x2, y2))
            visited[x2][y2] = 1
            dfs(x2, y2)
    
    result = len(arr) + 1
    
    return result

arr2 = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == 1:
            result = dfs(i,j)
            arr.clear()
            arr2.append(result)

arr2.sort()
print(len(arr2))
for elem in arr2:
    print(elem)