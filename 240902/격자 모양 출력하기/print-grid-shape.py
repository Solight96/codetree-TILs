n, m = map(int, input().split())

v = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    v[x-1][y-1] = x*y

for i in range(n):
    for j in range(n):
        print(v[i][j], end=' ')
    print()