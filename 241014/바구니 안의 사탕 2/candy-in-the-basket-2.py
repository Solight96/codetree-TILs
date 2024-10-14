N, K = map(int, input().split())

arr = [0] * 401
arr2 = []

for _ in range(N):
    inform = tuple(map(int, input().split()))
    arr[inform[1] + 200] += inform[0]
    arr2.append(inform[1] + 200)

max_val = max(arr2)
result = 0

for i in range(K, max_val-K+2):
    num = 0
    for j in range(i-K, i+K+1):
        num += arr[j]
    
    result = max(result, num)

print(result)