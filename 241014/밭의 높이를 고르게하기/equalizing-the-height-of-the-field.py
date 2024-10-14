import sys

N, H, T = map(int, input().split())

height = list(map(int, input().split()))

result = sys.maxsize

for i in range(N-T+1):
    cost = 0
    for j in range(i, i+T):
        cost += abs(height[j] - H)
    
    result = min(result, cost)

print(result)