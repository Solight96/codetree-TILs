n, m, r, c = map(int, input().split())
r, c = r-1, c-1

v = [[0] * n for _ in range(n)]

direct = list(input().split())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dice = [[0,2,0],[4,6,3],[0,5,0]]

drs = [-1,0,1,0]
dcs = [0,1,0,-1]

v[r][c] = 6

for j in range(m):
    if direct[j] == 'U': i = 0
    elif direct[j] == 'R': i = 1
    elif direct[j] == 'D': i = 2
    elif direct[j] == 'L': i = 3
    
    nr, nc = r+drs[i], c+dcs[i]
    
    if in_range(nr, nc):
        r, c = nr, nc
        if direct[j] == 'U':
            dice[0][1],dice[1][1],dice[2][1] = dice[1][1],dice[2][1],7-dice[1][1]
        elif direct[j] == 'R':
            dice[1] = [dice[1][1], dice[1][2], 7-dice[1][1]]
        elif direct[j] == 'D':
            dice[0][1],dice[1][1],dice[2][1] = 7-dice[1][1],dice[0][1],dice[1][1]
        elif direct[j] == 'L':
            dice[1] = [7-dice[1][1],dice[1][0],dice[1][1]]

    v[r][c] = dice[1][1]

result = 0

for i in range(n):
    for j in range(n):
        result += v[i][j]

print(result)