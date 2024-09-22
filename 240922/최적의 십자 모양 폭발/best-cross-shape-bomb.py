import copy

n = int(input())

v =[list(map(int, input().split())) for _ in range(n)]
w = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0

for i in range(n):
    for j in range(n):
        v2 = copy.deepcopy(v)
        l = v[i][j]

        for x in range(i-l+1, i+l):
            if in_range(x, j):
                v2[x][j] = 0
        for y in range(j-l+1, j+l):
            if in_range(i, y):
                v2[i][y] = 0
        # 폭탄 터짐

        for y in range(n):
            cnt = n-1
            for x in range(n-1, -1, -1):
                if v2[x][y] != 0:
                    w[cnt][y] = v2[x][y]
                    cnt -= 1
        # 중력 작용
        
        num = 0

        for x in range(n):
            for y in range(n-1):
                if (w[x][y] + w[x][y+1]) != 0 and w[x][y] == w[x][y+1]:
                    num += 1
        
        for y in range(n):
            for x in range(n-1):
                if (w[x][y] + w[x+1][y]) != 0 and w[x][y] == w[x+1][y]:
                    num += 1
        # 쌍 개수 측정

        w = [[0] * n for _ in range(n)]

        if result <= num:
            result = num

print(result)