n, t = map(int, input().split())

belt1 = list(map(int, input().split()))
belt2 = list(map(int, input().split()))
belt3 = list(map(int, input().split()))

arr = belt1 + belt2 + belt3

for _ in range(t):
    temp = arr[-1]
    for i in range(3*n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

print(*arr[:n])
print(*arr[n:2*n])
print(*arr[2*n:])