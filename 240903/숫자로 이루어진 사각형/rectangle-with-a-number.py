def square(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            print("{} ".format(cnt), end='')
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

N = int(input())

square(N)