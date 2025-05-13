a, b = map(int, input().split())

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

num = []

for i in range(a, b+1):
    if is_prime(i):
        num.append(i)

result = 0

for elem in num:
    m = elem // 10
    n = elem % 10
    if (m+n) % 2 == 0:
        result += 1

print(result)