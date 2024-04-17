N = int(input())

a = []

for _ in range(N):
    a.append(int(input()))

for i in range(len(a)):
    if a[i]%2 == 1 and a[i]%3 == 0:
        print(a[i])