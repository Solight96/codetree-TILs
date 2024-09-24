n = int(input())

v = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

def pinball(x,y):
    t = 1
    arr = []
    finish = False

    if x == 0:
        direct = 2
        while not finish:
            nx, ny = x+dxs[direct%4], y+dys[direct%4]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if direct%2 == 0 and v[x][y] == 1:
                    direct += 1
                elif direct%2 == 0 and v[x][y] == 2:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 1:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 2:
                    direct += 1
            else:
                arr.append(t)
                finish = True
            
    elif x == n-1:
        direct = 0
        while not finish:
            nx, ny = x+dxs[direct%4], y+dys[direct%4]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if direct%2 == 0 and v[x][y] == 1:
                    direct += 1
                elif direct%2 == 0 and v[x][y] == 2:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 1:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 2:
                    direct += 1
            else:
                arr.append(t)
                finish = True

    if y == 0:
        direct = 1
        while not finish:
            nx, ny = x+dxs[direct%4], y+dys[direct%4]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if direct%2 == 0 and v[x][y] == 1:
                    direct += 1
                elif direct%2 == 0 and v[x][y] == 2:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 1:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 2:
                    direct += 1
            else:
                arr.append(t)
                finish = True

    elif y == n-1:
        direct = 3
        while not finish:
            nx, ny = x+dxs[direct%4], y+dys[direct%4]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if direct%2 == 0 and v[x][y] == 1:
                    direct += 1
                elif direct%2 == 0 and v[x][y] == 2:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 1:
                    direct += 3
                elif direct%2 != 0 and v[x][y] == 2:
                    direct += 1
            else:
                arr.append(t)
                finish = True
    else:
        arr.append(0)
    
    return max(arr)

arr2 = []

for i in range(n):
    for j in range(n):
        result = pinball(i,j)
        arr2.append(result)

print(max(arr2))