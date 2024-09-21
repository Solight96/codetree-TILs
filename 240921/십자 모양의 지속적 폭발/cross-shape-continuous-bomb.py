import copy

n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]
v2 = [[0] * n for _ in range(n)]

arr = []

for _ in range(m):
    arr.append(int(input()))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for k in range(len(arr)):
    j = arr[k]
    
    for i in range(n):
        if v[i][j-1] != 0:
            l = v[i][j-1]
            break
        if i == n-1:
            l = 0
    
    if l != 0:
        for a in range(i-l+1, i+l):
            if in_range(a, j-1):
                v[a][j-1] = 0
        
        for b in range(j-l, j-1+l):
            if in_range(i, b):
                v[i][b] = 0
        # 0으로 빵꾸뚫기 완료

        for M in range(n):
            cnt = n-1
            for N in range(n-1, -1, -1):
                if v[N][M] != 0:
                    v2[cnt][M] = v[N][M]
                    cnt -= 1

        v = copy.deepcopy(v2)
        # v = v2
        v2 = [[0] * n for _ in range(n)]

for elem in v:
    print(*elem)