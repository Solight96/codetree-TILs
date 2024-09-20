n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

s1, e1 = map(int, input().split())

temp = []
for i in range(n):
    if s1-1<= i and i < e1:
        continue
    else:
        temp.append(arr[i])

arr = temp

s2, e2 = map(int, input().split())

temp = []
for i in range(len(arr)):
    if s2-1<= i and i < e2:
        continue
    else:
        temp.append(arr[i])

arr = temp

print(len(arr))
for elem in arr:
    print(elem)