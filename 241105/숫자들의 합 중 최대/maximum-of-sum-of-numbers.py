X, Y = map(int, input().split())

result = 0

for i in range(X, Y+1):
    result = max(result, sum(list(map(int, list(str(i))))))

print(result)