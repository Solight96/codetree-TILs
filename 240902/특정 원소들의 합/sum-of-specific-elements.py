v = [list(map(int, input().split())) for _ in range(4)]
add = 0

for i in range(4):
    for j in range(4):
        if i>=j:
            add += v[i][j]
print(add)