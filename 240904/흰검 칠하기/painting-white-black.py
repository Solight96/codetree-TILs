n = int(input())
loc = [0] * (200 * n)
x = 0
cnt_b = [0] * (200 * n)
cnt_w = [0] * (200 * n)

for _ in range(n):
    order = input().split()

    if order[1] == 'R':
        nx = x + int(order[0])
        for i in range(x+100*n, nx+100*n):
            if (cnt_w[i] >= 2 and cnt_b[i] >= 1) or loc[i] == 'G':
                loc[i] = 'G'
            else:
                loc[i] = 'B'
                cnt_b[i] += 1
        x = nx - 1
    elif order[1] == 'L':
        nx = x - int(order[0])
        for i in range(x+100*n, nx+100*n, -1):
            if (cnt_b[i] >= 2 and cnt_w[i] >= 1) or loc[i] == 'G':
                loc[i] = 'G'
            else:
                loc[i] = 'W'
                cnt_w[i] += 1
        x = nx + 1

print(loc.count('W'), loc.count('B'), loc.count('G'))