N, M, K = map(int, input().split())

v = [[0] * N for _ in range(N)]

for _ in range(M):
    r,c = map(int, input().split())
    v[r-1][c-1] = 1 # 1은 사과

x, y = 0, 0
t = 0
arr = []
arr.append((x,y))
finish = False

v[x][y] = 2 # 2는 뱀

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

for _ in range(K):
    d,p = input().split()

    if d == 'U':
        for _ in range(int(p)):
            nx, ny = x + dxs[0], y + dys[0]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if v[x][y] == 2:
                    finish = True
                    break # 게임 종료(몸 꼬임)
                elif v[x][y] == 1:
                    v[x][y] = 2
                    arr.append((x, y))
                else:
                    v[x][y] = 2
                    arr.append((x, y))
                    v[arr[0][0]][arr[0][1]] = 0
                    arr.pop(0)
            else:
                finish = True
                break # 게임 종료(격자 밖)

    elif d == 'R':
        for _ in range(int(p)):
            nx, ny = x + dxs[1], y + dys[1]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if v[x][y] == 2:
                    finish = True
                    break # 게임 종료(몸 꼬임)
                elif v[x][y] == 1:
                    v[x][y] = 2
                    arr.append((x, y)) 
                else:
                    v[x][y] = 2
                    arr.append((x, y))
                    v[arr[0][0]][arr[0][1]] = 0
                    arr.pop(0)           
            else:
                finish = True
                break # 게임 종료(격자 밖)
    
    elif d == 'D':
        for _ in range(int(p)):
            nx, ny = x + dxs[2], y + dys[2]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if v[x][y] == 2:
                    finish = True
                    break # 게임 종료(몸 꼬임)
                elif v[x][y] == 1:
                    v[x][y] = 2
                    arr.append((x, y)) 
                else:
                    v[x][y] = 2
                    arr.append((x, y))
                    v[arr[0][0]][arr[0][1]] = 0
                    arr.pop(0)
            else:
                finish = True
                break # 게임 종료(격자 밖)
    
    elif d == 'L':
        for _ in range(int(p)):
            nx, ny = x + dxs[3], y + dys[3]
            t += 1
            if in_range(nx, ny):
                x, y = nx, ny
                if v[x][y] == 2:
                    finish = True
                    break # 게임 종료(몸 꼬임)
                elif v[x][y] == 1:
                    v[x][y] = 2
                    arr.append((x, y))
                else:
                    v[x][y] = 2
                    arr.append((x, y))
                    v[arr[0][0]][arr[0][1]] = 0
                    arr.pop(0)
            else:
                finish = True
                break # 게임 종료(격자 밖)
    
    if finish:
        break

print(t)