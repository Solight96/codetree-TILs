N, T = map(int, input().split())

string = str(input())

v = [[0]*N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = N//2, N//2

dir_num = 0
result = 0

def in_range(x, y):
    return 0<=x and x<N and 0<=y and y<N

for i in range(N):
    num = list(map(int, input().split()))
    v[i] = num

result += v[x][y]
for j in range(T):
    if string[j] == 'L':
        dir_num = (dir_num+3)%4
    elif string[j] == 'R':
        dir_num = (dir_num+1)%4
    elif string[j] == 'F':
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx, ny):
            x = x + dx[dir_num]
            y = y + dy[dir_num]
            result += v[x][y]

print(result)