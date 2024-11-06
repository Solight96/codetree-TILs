N = int(input())

arr = list(input())

num = 0
x, y = 0, 0
num_list = []

for i in range(len(arr)):
    if arr[i] == '0':
        arr[i] = '1'
        for j in range(len(arr)-1):
            if arr[j] == '1':
                cnt = 0
                for k in range(j+1, len(arr)):
                    if arr[k] == '0':
                        cnt += 1
                    else:
                        cnt += 1
                        break
        print(arr)
        print(cnt)
        if num < cnt:
            num = cnt
            x = j
            y = k

    num_list.append((num, j, k))

print(num_list)

# num2 = 1000000

# for i in range(len(arr)-1):
#     if arr[i] == '1':
#         cnt = 0
#         for j in range(i+1, len(arr)):
#             if j == len(arr)-1 and arr[j] == '0':
#                 cnt = 1000000
#             else:
#                 if arr[j] != '1':
#                     cnt += 1
#                 else:
#                     cnt += 1
#                     break

#         if num2 > cnt:
#             num2 = cnt

# print(num2)