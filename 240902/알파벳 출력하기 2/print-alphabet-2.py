N = int(input())

cnt = 65

for i in range(N):
    print("  "*i, end='')
    for _ in range(N-i):
        print(chr(cnt), end=' ')
        cnt += 1
        if cnt == 91:
            cnt == 65
    print()