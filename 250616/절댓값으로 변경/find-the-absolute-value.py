n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = abs(arr[i])

print(*arr)