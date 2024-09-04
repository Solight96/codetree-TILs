N = int(input())

v = [[0] * 200 for _ in range(200)]
result = 0

for _ in range(N):
    x1, y1 = map(int, input().split())
    for i in range(x1+100, x1+108):
        for j in range(y1+100, y1+108):
            v[i][j] = 1

for elem in v:
    result += elem.count(1)
print(result)