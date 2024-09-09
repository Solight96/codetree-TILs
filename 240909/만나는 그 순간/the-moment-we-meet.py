N, M = map(int, input().split())

arr_A = []
arr_B = []

loc_A = 0
loc_B = 0

for _ in range(N):
    A = (input().split())
    if A[0] == 'L':
        for _ in range(int(A[1])):
            loc_A -= 1
            arr_A.append(loc_A)
    elif A[0] == 'R':
        for _ in range(int(A[1])):
            loc_A += 1
            arr_A.append(loc_A)

for _ in range(M):
    B = (input().split())
    if B[0] == 'L':
        for _ in range(int(B[1])):
            loc_B -= 1
            arr_B.append(loc_B)
    elif B[0] == 'R':
        for _ in range(int(B[1])):
            loc_B += 1
            arr_B.append(loc_B)

for i in range(len(arr_A)):
    if arr_A[i] == arr_B[i]:
        print(i+1)
        break
    elif i == (len(arr_A) - 1):
        print(-1)