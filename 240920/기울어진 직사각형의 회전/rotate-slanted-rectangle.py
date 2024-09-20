n = int(input())

v = [list(map(int, input().split())) for _ in range(n)]

r, c, m1, m2, m3, m4, direct = map(int, input().split())

drs, dcs = [-1, -1, 1, 1], [1, -1, -1, 1]
length = [m1, m2, m3, m4]
arr = []

for dr, dc, l in zip(drs, dcs, length):
    for _ in range(l):
        arr.append(v[r-1][c-1])
        r += dr
        c += dc


if direct == 0:
    temp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp
    
    i = 0
    for dr, dc, l in zip(drs, dcs, length):
        for _ in range(l):
            v[r-1][c-1] = arr[i]
            r += dr
            c += dc
            i += 1

elif direct == 1:
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    
    i = 0
    for dr, dc, l in zip(drs, dcs, length):
        for _ in range(l):
            v[r-1][c-1] = arr[i]
            r += dr
            c += dc
            i += 1

for elem in v:
    print(*elem)