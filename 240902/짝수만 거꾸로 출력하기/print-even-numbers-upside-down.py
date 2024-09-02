n = int(input())
result = []

input_list = list(map(int, input().split()))

for i in range(n):
    if input_list[i]%2 == 0:
        result.append(input_list[i])
result.reverse()

for i in range(len(result)):
    print(result[i], end = ' ')