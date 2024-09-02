n = int(input())
result = 1e10

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        sub = abs(i-j)
        if sub <= result:
            result = sub
print(result)