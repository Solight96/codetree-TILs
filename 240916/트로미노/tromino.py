n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]

def rec(v, row_s, row_e, col_s, col_e, n, m):
    num_r = 0
    num_c = 0
    for i in range(row_s, row_e+1):
        if col_e > m:
            num_r = 0
        num_c += v[i][col_s]
    for j in range(col_s, col_e+1):
        if row_e > n:
            num_c = 0
        num_r += v[row_s][j]
    
    return max(num_r, num_c)

def tri(v, row_s, row_e, col_s, col_e):
    num = 0
    arr = []
    for i in range(row_s, row_e+1):
        for j in range(col_s, col_e+1):
            num += v[i][j]
            arr.append(v[i][j])

    return num - min(arr)

result = 0

for i in range(n):
    for j in range(m):
        if i+2 < n or j+2 < m:
            rec_result = rec(v,i,i+2,j,j+2, n, m)
        if i+1 < n or j+1 < m:
            tri_result = tri(v,i,i+1,j,j+1)
        result = max(result, max(tri_result, rec_result))

print(result)