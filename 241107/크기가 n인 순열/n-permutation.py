n = int(input())

arr = []
visited = [0] * (n+1)

def choose(idx):
    if idx == n+1:
        for elem in arr:
            print(elem, end=' ')
        print()
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = 1
        arr.append(i)
        
        choose(idx+1)

        arr.pop()
        visited[i] = 0

choose(1)