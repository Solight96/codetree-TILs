R, C = map(int, input().split())

board = [list(input().split()) for _ in range(R)]

m, n, cnt = 0, 0, 0
arr = []

arr.append((m,n,cnt))

while True:
    m, n, cnt = arr.pop(0)
    if cnt == 2:
        break

    for i in range(m+1, R-1):
        for j in range(n+1, C-1):
            if board[m][n] != board[i][j]:
                arr.append((i,j,cnt+1))

print(len(arr)+1)