from collections import deque
import sys

N = int(input())

q = deque()

for _ in range(N):
    p = int(input()) # 각 방마다의 인원 수
    q.append(p)

result = sys.maxsize

for i in range(N):
    num = 0
    for j in range(N):
        num += j * q[j]
    if num < result:
        result = num
    q.rotate(-1)

print(result)