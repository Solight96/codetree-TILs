N, M, Q = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(N)]

arr = []

for _ in range(Q):
    r, d = input().split()
    arr.append([r, d])

def wind(i, p):
    if arr[i][1] == 'L':
        temp = v[p][-1]
        for k in range(M-1, 0, -1):
            v[p][k] = v[p][k-1]
        v[p][0] = temp
        chk[p] = 1

        for j in range(M):
            if p >= 1 and chk[p-1] == 0 and v[p][j] == v[p-1][j]:
                arr[i][1] = 'R'
                wind(i, p-1)
            if p <= N-2 and chk[p+1] == 0 and v[p][j] == v[p+1][j]:
                arr[i][1] = 'R'
                wind(i, p+1)

    elif arr[i][1] == 'R':
        temp = v[p][0]
        for k in range(M-1):
            v[p][k] = v[p][k+1]
        v[p][-1] = temp
        chk[p] = 1

        for j in range(M):
            if p >= 1 and chk[p-1] == 0 and v[p][j] == v[p-1][j]:
                arr[i][1] = 'L'
                wind(i, p-1)
            if p <= N-2 and chk[p+1] == 0 and v[p][j] == v[p+1][j]:
                arr[i][1] = 'L'
                wind(i, p+1)

for i in range(len(arr)):
    chk = [0] * N
    wind(i, int(arr[i][0])-1)

for elem in v:
    print(*elem)