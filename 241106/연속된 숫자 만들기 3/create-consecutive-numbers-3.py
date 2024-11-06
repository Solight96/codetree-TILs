loc = list(map(int, input().split()))

d1 = loc[1] - loc[0]
d2 = loc[2] - loc[1]

cnt = 0

while not (d1 == 1 and d2 == 1):
    if d1 >= d2:
        d2 = 1
        d1 -= d2
    else:
        d1 = 1
        d2 -= d1
    cnt += 1

print(cnt)