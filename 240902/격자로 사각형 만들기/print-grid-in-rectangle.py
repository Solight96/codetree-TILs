n = int(input())

v = [[1 for _ in range(n)] for _ in range(n)]

x = 1
y = 1

for i in range(1, n):
    for j in range(1, n):
        v[i][j] = v[i-1][j] + v[i][j-1] + v[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(v[i][j], end=' ')
    print()