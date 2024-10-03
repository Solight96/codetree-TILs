from collections import deque

N = int(input())

dq = deque()

for i in range(N, 0, -1):
    dq.appendleft(i)


while len(dq) != 1:
    dq.popleft()
    dq.rotate(-1)

print(*dq)