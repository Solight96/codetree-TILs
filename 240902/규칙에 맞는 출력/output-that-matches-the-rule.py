N = int(input())

for i in range(N):
    for j in range(N):
        if i>=j:
            print(N+j-i, end=' ')
    print()