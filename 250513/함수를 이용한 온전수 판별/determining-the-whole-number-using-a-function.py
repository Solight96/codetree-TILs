a, b = map(int, input().split())

result = 0

for i in range(a, b+1):
    if i % 2 == 0 or (i % 5 == 0 and i % 10 != 0 ) or (i % 3 == 0 and i % 9 != 0):
        continue
    else:
        result += 1

print(result)