board = [list(map(int, input().split())) for _ in range(19)] # 검 : 1, 흰 : 2

result = 0

for i in range(19):
    for j in range(15):
        if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4]:
            if board[i][j] == 1:
                result = 1
                r, c = i+1, j+3
            elif board[i][j] == 2:
                result = 2
                r, c = i+1, j+3

for j in range(19):
    for i in range(15):
        if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j]:
            if board[i][j] == 1:
                result = 1
                r, c = i+3, j+1
            elif board[i][j] == 2:
                result = 2
                r, c = i+3, j+1

for i in range(15):
    for j in range(15):
        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4]:
            if board[i][j] == 1:
                result = 1
                r, c = i+3, j+3
            elif board[i][j] == 2:
                result = 2
                r, c = i+3, j+3

print(result)
print(r, c)