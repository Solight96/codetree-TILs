ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

v = [[0] * 2001 for _ in range(2002)]

for i in range(ax1+1000, ax2+1000):
    for j in range(ay1+1000, ay2+1000):
        v[i][j] = 1

for i in range(bx1+1000, bx2+1000):
    for j in range(by1+1000, by2+1000):
        v[i][j] = 0

x_min = 2001
y_min = 2001
x_max = 0
y_max = 0

for i in range(ax1+1000, ax2+1001):
    for j in range(ay1+1000, ay2+1001):
        if v[i][j] == 1:
            x_min = min(x_min, i)
            x_max = max(x_max, i)
            y_min = min(y_min, j)
            y_max = max(y_max, j)

print((x_max - x_min + 1)*(y_max - y_min + 1) if (x_min, y_min, x_max, y_max) != (2001, 2001, 0, 0) else 0)