n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

def in_range(nx, ny):
    return 0<=nx and nx<n and 0<=ny and ny<n

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

result = 0

for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and a[nx][ny] == 1:
                cnt += 1
        if cnt>=3:
            result += 1

print(result)