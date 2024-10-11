N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
num = 0

for i in range(N):
    for j in range(M-2):
        if board[i][j] == 'L' and board[i][j+1] == 'E' and board[i][j+2] == 'E':
            num += 1

for i in range(N):
    for j in range(2, M):
        if board[i][j] == 'L' and board[i][j-1] == 'E' and board[i][j-2] == 'E':
            num += 1

for j in range(M):
    for i in range(N-2):
        if board[i][j] == 'L' and board[i+1][j] == 'E' and board[i+2][j] == 'E':
            num += 1

for j in range(M):
    for i in range(2, N):
        if board[i][j] == 'L' and board[i-1][j] == 'E' and board[i-2][j] == 'E':
            num += 1

for i in range(N-2):
    for j in range(M-2):
        if board[i][j] == 'L' and board[i+1][j+1] == 'E' and board[i+2][j+2] == 'E':
            num += 1

for i in range(N-2):
    for j in range(2, M):
        if board[i][j] == 'L' and board[i+1][j-1] == 'E' and board[i+2][j-2] == 'E':
            num += 1

for i in range(2, N):
    for j in range(M-2):
        if board[i][j] == 'L' and board[i-1][j+1] == 'E' and board[i-2][j+2] == 'E':
            num += 1

for i in range(2, N):
    for j in range(2, M):
        if board[i][j] == 'L' and board[i-1][j-1] == 'E' and board[i-2][j-2] == 'E':
            num += 1

print(num)