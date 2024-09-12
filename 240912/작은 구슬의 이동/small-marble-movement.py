n, t = map(int, input().split())

r, c, d = map(str, input().split())

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

x, y = int(r), int(c)

if d == 'U':
    dir_num = 0
elif d == 'D':
    dir_num = 3
elif d == 'R':
    dir_num = 1
elif d == 'L':
    dir_num = 2


def in_range(nx, ny):
    return 1<=nx and nx<=n and 1<=ny and ny<=n

for _ in range(t):
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if not in_range(nx, ny):
        dir_num = (3 - dir_num)
        continue
    
    x = x + dx[dir_num]
    y = y + dy[dir_num]  

print(x, y)