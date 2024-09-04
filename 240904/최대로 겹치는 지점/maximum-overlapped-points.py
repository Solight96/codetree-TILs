n = int(input())
order = [0] * 100

for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1-1, x2):
        order[i] += 1

print(max(order))