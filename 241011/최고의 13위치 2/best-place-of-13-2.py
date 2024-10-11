N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

num = 0
result = 0

for i in range(N):
    for j in range(N-2):
        num += board[i][j] + board[i][j+1] + board[i][j+2]
        visited[i][j], visited[i][j+1], visited[i][j+2] = 1, 1, 1

        for k in range(N):
            for l in range(N-2):
                if not visited[k][l] + visited[k][l+1] + visited[k][l+2]:
                    num += board[k][l] + board[k][l+1] + board[k][l+2]
        
        if num > result:
            result = num
        
        num = 0
        visited = [[0] * N for _ in range(N)]

print(result)