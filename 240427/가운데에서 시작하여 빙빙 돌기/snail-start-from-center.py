n = int(input())

v = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
dir_num = 1
t = 1
cng = 0

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n

x, y = n//2, n//2

for i in range(1, n**2+1):
    v[x][y] = i
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if in_range(nx,ny):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        cnt += 1
        if cnt == t**2 or cnt == t**2+t:
            dir_num = (dir_num+3)%4
            cng += 1
            if cng == 2:
                t += 1
                cng = 0
    else:
        break


for i in range(n):
    for j in range(n):
        print(v[i][j], end = ' ')
    print()