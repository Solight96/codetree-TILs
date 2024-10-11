n, k = map(int, input().split())

arr = list(map(int, input().split()))

result = 0

for i in range(n-k):
    num = 0
    for j in range(i, i+k):
        num += arr[j]
        result = max(result, num)

print(result)