N = int(input())

x, y = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir_num = 0
t = 0
result = 0

for i in range(1, N+1):
    direct, dist = map(str, input().split())
    if direct == 'N':
        dir_num = 0
    elif direct == 'E':
        dir_num = 1
    if direct == 'S':
        dir_num = 2
    if direct == 'W':
        dir_num = 3
    for _ in range(int(dist)):
        x, y = x + dx[dir_num], y + dy[dir_num]
        t += 1
        if (x, y) == (0, 0):
            result = t
            break

if result != 0:
    print(result)
else:
    print(-1)