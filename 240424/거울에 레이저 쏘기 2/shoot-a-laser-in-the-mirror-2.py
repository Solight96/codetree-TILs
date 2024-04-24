N = int(input())

v = [[0] * N for _ in range(N)]

for i in range(N):
    mirror = str(input())
    for j in range(N):
        v[i][j] = mirror[j]

K = int(input())

def in_range(x, y):
    return 0<=x and x<N and 0<=y and y<N

cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir_num = (((K-1)//N)+2)%4

if (K-1)//N == 0:
    x, y = 0, (K-1)%N
elif (K-1)//N == 1:
    x, y = (K-1)%N, N-1
elif (K-1)//N == 2:
    x, y = N-1, (3*N-K)
elif (K-1)//N == 3:
    x, y = (4*N-K), 0

while True:
    if dir_num == 0 or dir_num == 2:
        if v[x][y] == '\\':
            dir_num = (dir_num+3)%4
        elif v[x][y] == '/':
            dir_num = (dir_num+1)%4
    elif dir_num == 1 or dir_num == 3:
        if v[x][y] == '\\':
            dir_num = (dir_num+1)%4
        elif v[x][y] == '/':
            dir_num = (dir_num+3)%4
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    cnt += 1
    if in_range(nx, ny):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
    else:
        break
print(cnt)