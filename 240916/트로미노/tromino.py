n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]

def rec_r(row, col_s, col_e):
    num_r = 0
    
    for j in range(col_s, col_e+1):
        if col_e >= m:
            num_r = 0
            break
        num_r += v[row][j]
    
    return num_r

def rec_c(row_s, row_e, col):
    num_c = 0
    
    for i in range(row_s, row_e+1):
        if row_e >= n:
            num_c = 0
            break
        num_c += v[i][col]
    
    return num_c

def tri(row_s, row_e, col_s, col_e):
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
            rec_r_result = rec_r(i,j,j+2)
            rec_c_result = rec_c(i,i+2,j)
            rec_result = max(rec_r_result, rec_c_result)
        if i+1 < n and j+1 < m:
            tri_result = tri(i,i+1,j,j+1)
        result = max(result, max(tri_result, rec_result))

print(result)