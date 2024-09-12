N = str(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
dir_num = 1

for i in range(len(N)):
    if N[i] == 'L':
        dir_num = (dir_num + 3)%4
    elif N[i] == 'R':
        dir_num = (dir_num + 1)%4
    else:
        dir_num = dir_num
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)