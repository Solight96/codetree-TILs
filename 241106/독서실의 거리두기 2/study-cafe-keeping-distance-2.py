N = int(input())

arr = list(input())

num = 0
x, y, = 0, 0

for i in range(len(arr)-1):
    cnt = 0
    if arr[i] == '1':
        for j in range(i+1, len(arr)):
            if arr[j] != '1':
                cnt += 1
            else:
                cnt += 1
                break
    if cnt != 0:
        cnt_c = cnt
    if num < cnt_c:
        num = cnt_c
        x = i
        y = j

if arr[-1] == '1':
    arr[(x+y)//2] = '1'
else:
    if cnt_c < y - (x+y)//2 or cnt_c < (x+y)//2 - x:
        arr[(x+y)//2] = '1'
    else:
        arr[-1] = '1'

num2 = 1000000

for i in range(len(arr)-1):
    if arr[i] == '1':
        cnt = 0
        for j in range(i+1, len(arr)):
            if j == len(arr)-1 and arr[j] == '0':
                cnt = 1000000
            else:
                if arr[j] != '1':
                    cnt += 1
                else:
                    cnt += 1
                    break

        if num2 > cnt:
            num2 = cnt

print(num2)