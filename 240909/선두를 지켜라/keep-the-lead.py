N, M = map(int, input().split())

loc_A = 0
loc_B = 0

arr_A = []
arr_B = []

for _ in range(N):
    A = (input().split())
    for _ in range(int(A[1])):
        loc_A += int(A[0])
        arr_A.append(loc_A)

for _ in range(M):
    B = (input().split())
    for _ in range(int(B[1])):
        loc_B += int(B[0])
        arr_B.append(loc_B)

cnt = 0

for i in range(len(arr_A)):
    if i == 0:
        if arr_A[i] > arr_B[i]:
            sign = 1
        elif arr_A[i] < arr_B[i]:
            sign = -1
        else:
            sign = 0
    else:
        if arr_A[i] > arr_B[i]:
            if sign == 0:
                sign = 1
            elif sign == -1:
                sign = 1
                cnt += 1
        elif arr_A[i] < arr_B[i]:
            if sign == 0:
                sign = -1
            elif sign == 1:
                sign = -1
                cnt += 1

print(cnt)