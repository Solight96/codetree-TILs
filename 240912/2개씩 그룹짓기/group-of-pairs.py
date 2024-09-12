N = int(input())

num = list(map(int, input().split()))

num.sort()
arr = []

for i in range(N):
    value = num[i] + num[(2*N-1)-i]
    arr.append(value)

arr.sort()
print(arr[-1])