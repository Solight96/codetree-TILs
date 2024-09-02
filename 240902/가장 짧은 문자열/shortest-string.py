arr = []

for _ in range(3):
    string = str(input())
    arr.append(len(string))

print(max(arr) - min(arr))