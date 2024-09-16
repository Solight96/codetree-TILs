n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]
# chk = [[0] * n for _ in range(n)]

# drs = [0, -1, 0, 1, 0]
# dcs = [0, 0, 1, 0, -1]

# def in_range (r, c):
#     return 0 <= r and r < n and 0 <= c and c < n

# def get_gold(r, c, k):
#     o_r, o_c = r, c
#     c_r, c_c = r, c
#     nc_r, nc_c = r, c

#     if k == 0:
#         return v[c_r][c_c]
    
#     num = 0
#     for dr, dc in zip(drs, dcs):
#         if in_range(nc_r, nc_c) and chk[nc_r][nc_c] == 0:
#             num += v[nc_r][nc_c]
#             chk[nc_r][nc_c] = 1
#         nc_r = c_r + dr
#         nc_c = c_c + dc
    
#     k -= 1
#     if k > 0:
#         for i in range(n):
#             for j in range(n):
#                 if v[i][j] == 1:
#                     get_gold(i,j,k)
    
#     return num

# result = get_gold(n//2, n//2, 2)
# print(result)
# --------------------------------------------------------
def in_range (r, c):
    return 0 <= r and r < n and 0 <= c and c < n

def get_gold_in_border(r, c, k):
    # 방향에 따라 바뀌는 dr,dc
    drs, dcs = [1, 1, -1, -1],[-1, 1, 1, -1]
    if k == 0:
        return v[r][c]
    num_gold  = 0
    c_r, c_c = r-k, c
    for dr, dc in zip(drs, dcs):
        for step in range(k):
            if in_range(c_r, c_c):
                num_gold += v[c_r][c_c]
            c_r += dr
            c_c += dc
    return num_gold

gold = 0
arr = []

k = n//2
for i in range(k+1):
    gold += get_gold_in_border(n//2, n//2, i)
    gain = gold * m - (k ** 2 + (k+1) ** 2)
    if gain >= 0:
        arr.append(gold)

print(max(arr))