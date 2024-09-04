n = int(input())
loc = [0] * (10 * n * 2)

x = 0

for _ in range(n):
    order = input().split()
    if order[1] == 'R':
        nx = x + int(order[0])
        for i in range(x+10*n, nx+10*n):
            loc[i] += 1
        x = nx
    else:
        nx = x - int(order[0])
        for i in range(nx+10*n, x+10*n):
            loc[i] += 1
        x = nx

cnt = 0

for elem in loc:
    if elem >= 2:
        cnt +=1

print(cnt)