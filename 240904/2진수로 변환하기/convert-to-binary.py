n = int(input())
arr = []

while True:
    if n<2:
        arr.append(n)
        break
    arr.append(n%2)
    n = n // 2

for digit in arr[::-1]:
    print(digit, end="")