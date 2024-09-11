n = int(input())

arr = []

for _ in range(n):
    word = input()
    arr.append(word)

arr.sort()

for elem in arr:
    print(elem)