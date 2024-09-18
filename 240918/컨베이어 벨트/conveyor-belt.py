n, t = map(int, input().split())

belt1 = list(map(int, input().split()))
belt2 = list(map(int, input().split()))

arr = belt1+belt2

for _ in range(t):
    temp = arr[-1]
    for i in range(2*n-1, 0, -1):
        arr[i] = arr[i-1]
        arr[0] = temp

print(*arr[:3])
print(*arr[3:])