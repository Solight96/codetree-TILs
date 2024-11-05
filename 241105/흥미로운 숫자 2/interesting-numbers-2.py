X, Y = map(int, input().split())

result = 0

for i in range(X, Y+1):
    arr = list(map(int, str(i)))
    digit = [0] * 10
    for j in range(len(arr)):
        digit[arr[j]] += 1
    if 1 in digit and digit.count(0) == 8:
        result += 1

print(result)