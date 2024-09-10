N, M = map(int, input().split())

loc_A = 0
arr_A = []
loc_B = 0
arr_B = []

for _ in range(N):
    A = tuple(map(int, input().split()))
    for _ in range(A[1]):
        loc_A += A[0]
        arr_A.append(loc_A)

for _ in range(M):
    B = tuple(map(int, input().split()))
    for _ in range(B[1]):
        loc_B += B[0]
        arr_B.append(loc_B)

win = 'AB'
cnt = 0

for i in range(len(arr_A)):
    if arr_A[i] > arr_B[i]:
        if win != 'A':
            win = 'A'
            cnt += 1
    elif arr_A[i] < arr_B[i]:
        if win != 'B':
            win = 'B'
            cnt += 1
    else:
        if win != 'AB':
            win = 'AB'
            cnt += 1

print(cnt)