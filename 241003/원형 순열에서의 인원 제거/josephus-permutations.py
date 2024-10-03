from collections import deque

N, K = map(int,input().split())
q = deque()

for i in range(1, N+1):
    q.append(i)

num = 1
arr = []

while q:
    if num == K:
        n = q.popleft()
        arr.append(n)
        num = 1
    else:
        q.rotate(-1)
        num += 1

print(*arr)