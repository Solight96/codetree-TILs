N, M, K = map(int, input().split())

arr = [0] * N

for i in range(M):
    num = int(input())
    arr[num-1] += 1
    if arr[num-1] == K:
        print(num)
        break
    elif i == M-1:
        print(-1)