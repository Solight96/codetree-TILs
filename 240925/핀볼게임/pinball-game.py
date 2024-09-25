n = int(input())

v = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

def pinball(x,y):
    t = 1
    finish = False

    if x == 0:
        direct = 2
    elif x == n-1:
        direct = 0
    elif y == 0:
        direct = 1
    elif y == n-1:
        direct = 3

    if direct%2 == 0:
        if v[x][y] == 1: direct += 1
        elif v[x][y] == 2: direct += 3
    else:
        if v[x][y] == 1: direct += 3
        elif v[x][y] == 2: direct += 1

    while not finish:
        nx, ny = x+dxs[direct%4], y+dys[direct%4]
        t += 1
        if in_range(nx, ny):
            x, y = nx, ny
            if direct%2 == 0:
                if v[x][y] == 1: direct += 1
                elif v[x][y] == 2: direct += 3
            else:
                if v[x][y] == 1: direct += 3
                elif v[x][y] == 2: direct += 1
        else:
            finish = True
            
    return t

arr = []

for i in range(n):
    result1 = pinball(i,0)
    result2 = pinball(i,n-1)
    arr.append(result1)
    arr.append(result2)
for j in range(n):
    result1 = pinball(0,j)
    result2 = pinball(n-1,j)
    arr.append(result1)
    arr.append(result2)

print(max(arr))