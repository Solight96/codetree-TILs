import copy

n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

result = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            arr2 = copy.deepcopy(arr)
            line = [0] * 101
            arr2.pop(k)
            arr2.pop(j)
            arr2.pop(i)
            for l in range(len(arr2)):
                x, y = arr2[l]
                for m in range(x, y+1):
                    line[m] += 1
            
            if max(line) == 1:
                result += 1

print(result)