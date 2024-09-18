n = int(input())
v = [list(map(int, input().split())) for _ in range(n)]


def in_range(r, c):
    return 0 <= r and r < n and 0 <= c and c < n


def rec(r, c, h, w):
    drs, dcs = [-1, -1, 1, 1], [1, -1, -1, 1]
    lengths = [h, w, h, w]
    
    num = 0

    for dr, dc, l in zip(drs, dcs, lengths):
        for _ in range(l):
            r = r + dr
            c = c + dc

            if not in_range(r, c):
                return 0
            
            num += v[r][c]
    
    return num

result = 0

for r in range(n):
    for c in range(n):
        for h in range(1, n):
            for w in range(1, n):
                result = max(result, rec(r, c, h, w))

print(result)