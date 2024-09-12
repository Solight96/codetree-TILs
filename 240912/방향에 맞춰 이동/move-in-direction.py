dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())

x = 0
y = 0

for _ in range(N):
    direction, scalar = map(str, input().split())
    if direction == 'N':
        x = x+int(scalar) * dx[0]
        y = y+int(scalar) * dy[0]
    elif direction == 'E':
        x = x+int(scalar) * dx[1]
        y = y+int(scalar) * dy[1]
    elif direction == 'S':
        x = x+int(scalar) * dx[2]
        y = y+int(scalar) * dy[2]
    else:
        x = x+int(scalar) * dx[3]
        y = y+int(scalar) * dy[3]

print(x, y)