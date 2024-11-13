N = int(input())

arr = list(input())

num = 0
x = 0
num_list = []

for i in range(len(arr)):
    if arr[i] == '0':
        arr[i] = '1'
        cnt_list = []
        for j in range(len(arr)-1):
            if arr[j] == '1':
                cnt = 0
                for k in range(j+1, len(arr)):
                    if arr[k] == '0':
                        if k == len(arr) - 1:
                            break
                        else:
                            cnt += 1
                    else:
                        cnt += 1
                        break
                cnt_list.append(cnt)
        if arr[-1] == '0':
            cnt_list.pop(-1)
        
        cnt = min(cnt_list)

        if num < cnt:
            num = cnt
            x = i
        num_list.append((num, x))
        arr[i] = '0'

num_list.sort()
x = num_list[-1][1]
arr[x] = '1'

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