N, K = map(int, input().split())

order = [0] * N

for _ in range(K):
    A, B = map(int, input().split())
    for i in range(A-1, B):
        order[i] += 1

print(max(order))