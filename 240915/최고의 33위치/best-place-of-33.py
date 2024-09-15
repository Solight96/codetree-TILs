N = int(input())

v = [list(map(int, input().split())) for _ in range(N)]

def max_coin(row_s, row_e, col_s, col_e):
    cnt = 0

    for i in range(row_s, row_e+1):
        for j in range(col_s, col_e+1):
            cnt += v[i][j]
    
    return cnt

result = 0

for i in range(N):
    for j in range(N):
        if i+2 >= N or j+2 >= N:
            continue
        num_coin = max_coin(i, i+2, j, j+2)

        result = max(result, num_coin)

print(result)