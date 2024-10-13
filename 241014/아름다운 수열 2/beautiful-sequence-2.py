N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

num = 0

for i in range(N-M+1):
    cnt = 0
    for j in range(i, i+M):
        if A[j] in B:
            cnt += 1
    if cnt == M:
        num += 1

print(num)