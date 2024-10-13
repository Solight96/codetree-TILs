import copy

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

num = 0

for i in range(N-M+1):
    C = copy.deepcopy(B)
    for j in range(i, i+M):
        if A[j] in C:
            C.pop(C.index(A[j]))
    if not len(C):
        num += 1

print(num)