n = int(input())

num_list = list(map(int, input().split()))

result = 0

for i in range(len(num_list)-1):
    for j in range(i+2, len(num_list)):
        num = num_list[i] + num_list[j]
        if result < num:
            result = num

print(result)