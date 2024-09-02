n, m = map(int, input().split())

v1 = [list(map(int, input().split())) for _ in range(n)]
v2 = [list(map(int, input().split())) for _ in range(n)]

result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if v1[i][j] == v2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()