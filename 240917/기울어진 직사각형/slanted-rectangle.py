n = int(input())
v = [list(map(int, input().split())) for _ in range(n)]

num = 0

def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n

drs, dcs = [-1,-1,1,1], [1,-1,-1,1]
c_r, c_c = r, c

def rec(r, c):
    for dr, dc in zip(drs, dcs):
        if in_range(c_r, c_c):
            num += v[c_r][c_c]
        else:
            num = 0
            break
        c_r = c_r + dr
        c_c = c_c + dc
    

    return num