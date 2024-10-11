R, C = map(int, input().split())

board = [list(input().split()) for _ in range(R)]

m, n, cnt = 0, 0, 0
arr = []

arr.append((m,n,cnt))

while True:
    m, n, cnt = arr.pop(0)
    if cnt == 2:
        arr.append((m,n,cnt))
        break

    for i in range(m+1, R-1):
        for j in range(n+1, C-1):
            if board[m][n] != board[i][j]:
                arr.append((i,j,cnt+1))

m, n, _ = arr[0]
if board[m][n] != board[R-1][C-1]:
    print(len(arr))
else:
    print(0)