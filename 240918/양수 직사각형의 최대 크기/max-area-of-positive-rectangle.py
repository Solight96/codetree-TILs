n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]

def posrec(i, j, k, l):
    for x in range(i, k+1):
        for y in range(j, l+1):
            if v[x][y] <= 0:
                return -1
    return (k-i+1) * (l-j+1)

num = []

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                num.append(posrec(i, j, k, l))

print(max(num))