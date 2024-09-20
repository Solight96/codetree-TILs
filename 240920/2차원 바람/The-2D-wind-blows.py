import copy

N, M, Q = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(N)]
v2 = []

arr = []

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    arr.append((r1, c1, r2, c2))

for _ in range(len(arr)):
    arr1 = v[r1-1][c1-1:c2] # >>
    arr2 = [v[i][c2-1] for i in range(r1-1,r2)] # VV
    arr3 = v[r2-1][c1-1:c2] # <<
    arr4 = [v[i][c1-1] for i in range(r1-1,r2)] # ^^

    for j in range(len(arr1)-1):
        v[r1-1][c1+j] = arr1[j]
    for j in range(len(arr2)-1):
        v[r1+j][c2-1] = arr2[j]
    for j in range(1, len(arr3)):
        v[r2-1][c1-2+j] = arr3[j]
    for j in range(1, len(arr4)):
        v[r1-2+j][c1-1] = arr4[j]
    # 회전완료
    v2 = copy.deepcopy(v)
    
    for n in range(r1-1, r2):
        for m in range(c1-1, c2):
            if n-1 < 0:
                if m-1 < 0:
                    v2[n][m] = (v[n][m]+v[n+1][m]+v[n][m+1]) // 3
                elif m+1 >= M:
                    v2[n][m] = (v[n][m]+v[n+1][m]+v[n][m-1]) // 3
                else:
                    v2[n][m] = (v[n][m]+v[n+1][m]+v[n][m+1]+v[n][m-1]) // 4
            elif n+1 >= N:
                if m-1 < 0:
                    v2[n][m] = (v[n][m]+v[n-1][m]+v[n][m+1]) // 3
                elif m+1 >= M:
                    v2[n][m] = (v[n][m]+v[n-1][m]+v[n][m-1]) // 3
                else:
                    v2[n][m] = (v[n][m]+v[n-1][m]+v[n][m+1]+v[n][m-1]) // 4
            elif m-1 < 0:
                v2[n][m] = (v[n][m]+v[n+1][m]+v[n-1][m]+v[n][m+1]) // 4
            elif m+1 >= M:
                v2[n][m] = (v[n][m]+v[n+1][m]+v[n-1][m]+v[n][m-1]) // 4
            else:
                v2[n][m] = (v[n][m]+v[n+1][m]+v[n-1][m]+v[n][m+1]+v[n][m-1]) // 5
    
for elem in v2:
    print(*elem)