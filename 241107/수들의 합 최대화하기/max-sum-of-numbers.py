n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
idx_list = [i for i in range(n)]

arr = []
result = []

def choose(idx):
    global result
    if idx == n:
        num = 0
        for i, elem in zip(idx_list, arr):
            num += board[i][elem]
        result.append(num)
        return
    
    for j in range(n):
        if visited[j]:
            continue
        visited[j] = 1
        arr.append(j)
        choose(idx+1)

        arr.pop()
        visited[j] = 0

choose(0)
print(max(result))