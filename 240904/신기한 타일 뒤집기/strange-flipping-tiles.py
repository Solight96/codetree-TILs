n = int(input())
x = 0
loc = [0] * (100 * n * 2)

for _ in range(n):
    order = input().split()
    if order[1] == 'R':
        nx = x + int(order[0])
        for i in range(x+100*n, nx+100*n):
            loc[i] = 'B'
        x = nx - 1
    elif order[1] == 'L':
        nx = x - int(order[0])
        for i in range(x+100*n, nx+100*n, -1):
            loc[i] = 'W'
        x = nx + 1

print(loc.count('W'), loc.count('B'))