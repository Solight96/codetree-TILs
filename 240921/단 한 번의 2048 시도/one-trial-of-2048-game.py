v = [list(map(int,input().split())) for _ in range(4)]
v2 = [[0] * 4 for _ in range(4)]
v3 = [[0] * 4 for _ in range(4)]

direct = input()

if direct == 'L':
    for i in range(4):
        cnt = 0
        for j in range(4):
            if v[i][j] != 0:
                v2[i][cnt] = v[i][j]
                cnt += 1
    
    for i in range(4):
        for j in range(3):
            if v2[i][j] == v2[i][j+1]:
                v2[i][j] *= 2
                v2[i][j+1] = 0

    for i in range(4):
        cnt = 0
        for j in range(4):
            if v2[i][j] != 0:
                v3[i][cnt] = v2[i][j]
                cnt += 1

elif direct == 'R':
    for i in range(4):
        cnt = 3
        for j in range(3, -1, -1):
            if v[i][j] != 0:
                v2[i][cnt] = v[i][j]
                cnt -= 1
    
    for i in range(4):
        for j in range(3, 0, -1):
            if v2[i][j] == v2[i][j-1]:
                v2[i][j] *= 2
                v2[i][j-1] = 0

    for i in range(4):
        cnt = 3
        for j in range(3, -1, -1):
            if v2[i][j] != 0:
                v3[i][cnt] = v2[i][j]
                cnt -= 1

elif direct == 'U':
    for j in range(4):
        cnt = 0
        for i in range(4):
            if v[i][j] != 0:
                v2[cnt][j] = v[i][j]
                cnt += 1
    
    for j in range(4):
        for i in range(3):
            if v2[i][j] == v2[i+1][j]:
                v2[i][j] *= 2
                v2[i+1][j] = 0

    for j in range(4):
        cnt = 0
        for i in range(4):
            if v2[i][j] != 0:
                v3[cnt][j] = v2[i][j]
                cnt += 1

elif direct == 'D':
    for j in range(4):
        cnt = 3
        for i in range(3, -1, -1):
            if v[i][j] != 0:
                v2[cnt][j] = v[i][j]
                cnt -= 1
    
    for j in range(4):
        for i in range(3, 0, -1):
            if v2[i][j] == v2[i-1][j]:
                v2[i][j] *= 2
                v2[i-1][j] = 0

    for j in range(4):
        cnt = 3
        for i in range(3, -1, -1):
            if v2[i][j] != 0:
                v3[cnt][j] = v2[i][j]
                cnt -= 1

for elem in v3:
    print(*elem)