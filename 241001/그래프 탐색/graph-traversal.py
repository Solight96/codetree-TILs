# N, M = map(int, input().split())

# board = [[0] * N for _ in range(N)]
# visited = [False] * N
# arr = []

# for _ in range(M):
#     x, y = map(int, input().split())
#     x, y = x-1, y-1
#     board[x][y] = 1
#     board[y][x] = 1

# def dfs(v):
#     visited[v] = True

#     for curr in range(N):
#         if board[v][curr] == 1 and not visited[curr]:
#             arr.append(curr)
#             visited[curr] = True
#             dfs(curr)
    
#     return len(arr)

# result = dfs(0)
# print(result)
# ------------------------------------------------

N, M = map(int, input().split())

board = [[]] * N
visited = [False] * N
arr = []

for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    board[x].append(y)
    board[y].append(x)

def dfs(v):
    visited[v] = True

    for curr in board[v]:
        if not visited[curr]:
            arr.append(curr)
            visited[curr] = True
            dfs(curr)
    
    return len(arr)

result = dfs(0)
print(result)