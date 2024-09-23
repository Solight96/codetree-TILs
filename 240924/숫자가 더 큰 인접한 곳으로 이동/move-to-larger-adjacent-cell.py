n, r, c = map(int, input().split())

r, c = r-1, c-1

v = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

num = v[r][c]
arr = []
arr.append(num)

while True:
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy

        if in_range(nx, ny) and num < v[nx][ny]:
            num = v[nx][ny]
            r, c = nx, ny
            arr.append(num)
            break

    if c != ny:
        break

print(*arr)