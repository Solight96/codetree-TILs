n = int(input())

people = list(map(int, input().split()))

num = 0
arr = []

for i in range(len(people)):
    for j in range(len(people)):
        num += abs(j-i) * people[j]
    arr.append(num)
    num = 0

print(min(arr))