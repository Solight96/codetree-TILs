loc = list(map(int, input().split()))

loc.sort()

d1 = loc[1] - loc[0]
d2 = loc[2] - loc[1]

cnt = 0

while not (d1 == 1 and d2 == 1):
    if d1 <= d2:
        if not d1 == 1:
            tmp = d1
            d1 = d1 // 2
            d2 = tmp - d1
        else:
            tmp = d2
            d2 = d2 // 2
            d1 = tmp - d2
        cnt += 1
    else:
        if not d2 == 1:
            tmp = d2
            d2 = d2 // 2
            d1 = tmp - d2
        else:
            tmp = d1
            d1 = d1 // 2
            d2 = tmp - d1
        cnt += 1

print(cnt)