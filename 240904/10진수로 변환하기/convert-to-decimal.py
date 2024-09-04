n = input()
result = 0

for i in range(len(n)):
    result = result * 2 + int(n[i])

print(result)