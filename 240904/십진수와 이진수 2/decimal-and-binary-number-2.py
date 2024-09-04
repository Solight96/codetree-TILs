N = input()
result = 0
arr= []

for i in range(len(N)):
    result = result * 2 + int(N[i])

result = result * 17

while True:
    if result < 2:
        arr.append(result)
        break
    arr.append(result%2)
    result = result // 2

for digit in arr[::-1]:
    print(digit, end='')