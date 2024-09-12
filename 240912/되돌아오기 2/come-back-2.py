order = str(input())

x, y = 0, 0
dx = [-1, 0 , 1, 0]
dy = [0, 1, 0 , -1]

dir_num = 0

for i in range(len(order)):
    if order[i] == 'L':
        dir_num = (dir_num + 3)%4
    elif order[i] == 'R':
        dir_num = (dir_num + 1)%4
    elif order[i] == 'F':
        x = x + dx[dir_num]
        y = y + dy[dir_num]
    
    if (x, y) == (0,0):
        print(i+1)
        break
    elif i < (len(order) - 1):
        continue
    else:
        print(-1)