n = int(input())
loc = [0] * (200 * n)
x = 0
cnt = [0] * (200 * n)

for _ in range(n):
    order = input().split()

    if order[1] == 'R':
        nx = x + int(order[0])
        for i in range(x+100*n, nx+100*n):
            if cnt[i] == 3 or loc[i] == 'G':
                loc[i] = 'G'
            else:
                loc[i] = 'B'
                cnt[i] += 1
        x = nx
    elif order[1] == 'L':
        nx = x - int(order[0])
        for i in range(nx+100*n, x+100*n):
            if cnt[i] == 3 or loc[i] == 'G':
                loc[i] = 'G'
            else:
                loc[i] = 'W'
                cnt[i] += 1
        x = nx

print(loc.count('W'), loc.count('B'), loc.count('G'))