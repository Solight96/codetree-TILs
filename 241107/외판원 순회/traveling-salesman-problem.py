n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
idx_list = [i for i in range(n)]

visited = [0] * n
visited[0] = 1

arr = []
result = []

def choose(idx):
    if idx == n:
        num = board[arr[-1]][0]
        a = 0
        for i in range(n-1):
            elem = arr[i] 
            num += board[a][elem]
            a = elem
        result.append(num)
        return
    
    for j in range(1, n):
        if visited[j]:
            continue
        
        visited[j] = 1
        arr.append(j)
        choose(idx+1)

        arr.pop()
        visited[j] = 0

choose(1)
print(min(result))