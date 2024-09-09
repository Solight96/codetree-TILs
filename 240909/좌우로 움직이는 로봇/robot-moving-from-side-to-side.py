n, m = map(int, input().split())

loc_A = 0
loc_B = 0

arr_A = []
arr_B = []

for _ in range(n):
    A = (input().split())
    if A[1] == 'L':
        for _ in range(int(A[0])):
            loc_A -= 1
            arr_A.append(loc_A)
    elif A[1] == 'R':
        for _ in range(int(A[0])):
            loc_A += 1
            arr_A.append(loc_A)

for _ in range(m):
    B = (input().split())
    if B[1] == 'L':
        for _ in range(int(B[0])):
            loc_B -= 1
            arr_B.append(loc_B)
    elif B[1] == 'R':
        for _ in range(int(B[0])):
            loc_B += 1
            arr_B.append(loc_B)

cnt = 0
maximum = max(len(arr_A), len(arr_B))
minimum = min(len(arr_A), len(arr_B))

for i in range(maximum):
    if i == 0 and arr_A[i] == arr_B[i]:
        cnt += 1
    elif i < minimum:
        if arr_A[i-1] != arr_B[i-1] and arr_A[i] == arr_B[i]:
            cnt += 1
    else:
        if len(arr_A) <= len(arr_B):
            if arr_A[-1] != arr_B[i-1] and arr_A[-1] == arr_B[i]:
                cnt += 1
        elif len(arr_A) > len(arr_B):
            if arr_A[i-1] != arr_B[-1] and arr_A[i] == arr_B[-1]:
                cnt += 1

print(cnt)