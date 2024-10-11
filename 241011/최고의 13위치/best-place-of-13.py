N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
maximum = 0

for i in range(N):
    for j in range(N-2):
        num = board[i][j] + board[i][j+1] + board[i][j+2]
        if num > maximum:
            maximum = num

print(maximum)