n = int(input())

elem = list(map(int, input().split()))

for i in range(len(elem)):
    for j in range(len(elem)-1-i):
        if elem[j] > elem[j+1]:
            tmp = elem[j]
            elem[j] = elem[j+1]
            elem[j+1] = tmp

print(*elem)