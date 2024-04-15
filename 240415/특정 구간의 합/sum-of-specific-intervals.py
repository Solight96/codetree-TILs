n, m = map(int, input().split())

A = list(map(int, input().split()))

def listsum(n,m):
    for i in range(m):
        a1, a2 = map(int, input().split())
        sum_ = 0
        for j in range(a1-1,a2):
            sum_ += A[j]
        print(sum_)

listsum(n,m)