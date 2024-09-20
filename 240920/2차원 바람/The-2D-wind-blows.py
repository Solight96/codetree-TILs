N, M, Q = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(N)]

arr = []

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    arr.append((r1, c1, r2, c2))

for i in range(len(arr)):
    arr1 = v[r1-1][c1-1:c2] # >>
    arr2 = [v[i][c2-1] for i in range(r1-1,r2)] # VV
    arr3 = v[r2-1][c1-1:c2] # <<
    arr4 = [v[i][c1-1] for i in range(r1-1,r2)] # ^^