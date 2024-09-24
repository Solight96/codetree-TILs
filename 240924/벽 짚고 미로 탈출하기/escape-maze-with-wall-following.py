N = int(input())

x, y = map(int, input().split())
x, y = x-1, y-1
r, c = x, y

v = [list(input()) for _ in range(N)]

dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

t = 0
i = 0
cnt = 0

while True:
    if cnt == 3 or ((x,y) == (r, c) and i%4 == 0 and i != 0):
        break
    nx, ny = x+dxs[i%4], y+dys[i%4]

    if in_range(nx, ny) and v[nx][ny] == '#':
        i += 1
        cnt += 1 
    else:
        x, y = nx, ny
        t += 1
        cnt = 0
        
        if not in_range(x, y):
            break

        if in_range(x+dxs[(i+3)%4], y+dys[(i+3)%4]) and v[x+dxs[(i+3)%4]][y+dys[(i+3)%4]] != '#':
            i += 3
            nx, ny = x+dxs[i%4], y+dys[i%4]
            x, y = nx, ny
            t += 1
            cnt = 0

if cnt == 3 or ((x,y) == (r, c) and i%4 == 0 and i != 0):
    print(-1)
else:
    print(t)