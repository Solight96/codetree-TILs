n = int(input())
order = [0] * 201

for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1+99, x2+100):
        order[i] += 1

print(max(order) - 1)