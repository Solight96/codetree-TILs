n, k, T = input().split()
arr = []

for _ in range(int(n)):
    word = input()
    if T == word[:len(T)]:
        arr.append(word)

arr.sort()

print(arr[int(k)-1])