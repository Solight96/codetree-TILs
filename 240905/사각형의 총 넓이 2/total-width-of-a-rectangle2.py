N = int(input())
result = 0

v = [[0] * 200 for _ in range(200)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            v[i][j] = 1

for elem in v:
    result += elem.count(1)
print(result)