import copy

N, B = map(int,input().split())

arr = []

for _ in range(N):
    arr.append(int(input()))

result = 0

for i in range(N):
    arr2 = copy.deepcopy(arr)
    arr2[i] /= 2
    arr2.sort()
    num = 0
    B2 = copy.deepcopy(B)
    for j in range(len(arr2)):
        B2 -= arr2[j]
        if B2 >= 0:
            num += 1
        else:
            result = max(result, num)
            break

print(result)