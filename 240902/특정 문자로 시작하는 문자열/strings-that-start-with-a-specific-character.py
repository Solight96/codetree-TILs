n = int(input())
arr = []
add = 0
cnt = 0

for _ in range(n):
    string = str(input())
    arr.append(string)

chk = str(input())

for i in range(len(arr)):
    if arr[i][0] == chk:
        add += len(arr[i])
        cnt += 1

print(cnt, end=' ')
print("{:.2f}".format(add / cnt))