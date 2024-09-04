a, b = map(int, input().split())

n = input()

result = 0
arr = []

for i in range(len(n)):
    result = result * a + int(n[i])

while True:
    if result < b:
        arr.append(result)
        break
    arr.append(result % b)
    result = result // b

for digit in arr[::-1]:
    print(digit, end='')