N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

num = 0

for i in range(N-M+1):
    C = [0] * M
    cnt = 0
    for j in range(i, i+M):
        if A[j] in B:
            C[B.index(A[j])] += 1
    for k in range(M):
        if C[k] >= 1:
            cnt += 1
    if cnt == M:
        num += 1

print(num)