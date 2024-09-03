def calc(n):
    add = 0
    for i in range(1, n+1):
        add += i
    return add // 10


N = int(input())
result = calc(N)
print(result)