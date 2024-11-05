X, Y = map(int, input().split())

cnt = 0

for i in range(X, Y+1):
    num = list(str(i))
    num_r = list(reversed(num))


    if num == num_r:
        cnt += 1

print(cnt)