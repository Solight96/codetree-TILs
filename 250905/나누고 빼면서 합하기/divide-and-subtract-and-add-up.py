n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def divsubsum(n,m):
    sum = 0
    while m != 1:
        sum += A[m-1]
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return sum + A[0]

result = divsubsum(n,m)
print(result)