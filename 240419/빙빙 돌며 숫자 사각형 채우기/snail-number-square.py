n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

x, y = 0, 0

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

answer = [[0] * m for _ in range(n)]
answer[x][y] = 1

dir_num = 1

for i in range(2, m*n + 1):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    x = x + dx[dir_num]
    y = y + dy[dir_num]
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()