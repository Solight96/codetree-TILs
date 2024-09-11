n = int(input())

a = list(map(int, input().split()))

result = []

for idx in range(len(a)):
    if idx%2 == 0:
        a_list = a[:idx+1]
        a_list.sort()
        result.append(a_list[idx//2])

for i in range(len(result)):
    print(result[i], end=' ')