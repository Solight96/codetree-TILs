n = int(input())

v = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * n for _ in range(n)]

r, c = map(int,input().split())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

size = v[r-1][c-1]

for i in range(-size+1, size):
    if in_range(r-1+i, c-1):
        v[r-1+i][c-1] = 0
    if in_range(r-1, c-1+i):
        v[r-1][c-1+i] = 0
# 폭탄터짐


for col in range(n):
    rowtemp = n-1
    for row in range(n-1, -1, -1):
        if v[row][col] != 0:
            temp[rowtemp][col] = v[row][col]
            rowtemp -= 1
# 중력발생

v = temp

for elem in v:
    print(*elem)