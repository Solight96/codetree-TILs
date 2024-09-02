n = int(input())

for i in range(1, n+1):
    for j in range(1, 7-i):
        if j == (6-i):
            print(f"{i} * {j} = {i * j}")
        else:
            print(f"{i} * {j} = {i * j}", end = ' / ')