a, b = map(int, input().split())

result = [0] * b

while 1:
    if a <= 1:
        break
    tmp = a//b
    i = a%b
    a = tmp
    result[i] += 1

add = 0
for i in range(len(result)):
    add += result[i] ** 2
print(add)