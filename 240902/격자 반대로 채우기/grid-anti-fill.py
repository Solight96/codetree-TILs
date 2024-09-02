n = int(input())
v = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1

x = n-1
y = n-1

for cnt in range(1, n ** 2+1):
    v[x][y] = cnt
    if y%2 != 0:
        x -= 1
        if x<0:
            x = 0
            y -= 1
    else:
        x += 1
        if x>3:
            x = 3
            y -= 1

for i in range(n):
    for j in range(n):
        print(v[i][j], end=' ')
    print()