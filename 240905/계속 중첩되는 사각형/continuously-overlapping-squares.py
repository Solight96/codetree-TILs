n = int(input())

v = [[0] * 201 for _ in range(202)]
arr = []

for _ in range(n):
    inform = tuple(map(int, input().split()))
    arr.append(inform)

for i in range(len(arr)):
    if i%2 == 0:
        for x in range(arr[i][0]+100, arr[i][2] + 100):
            for y in range(arr[i][1]+100, arr[i][3] + 100):
                v[x][y] = 'R'
    else:
        for x in range(arr[i][0]+100, arr[i][2] + 100):
            for y in range(arr[i][1]+100, arr[i][3] + 100):
                v[x][y] = 'B'

cnt = 0

for elem in v:
    cnt += elem.count('B')

print(cnt)