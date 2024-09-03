def prime(n):
    is_prime = True
    for i in range(2, n):
        if n%i == 0:
            is_prime = False
    return is_prime

a, b = map(int, input().split())
result = 0

for i in range(a, b+1):
    if prime(i):
        result += i

print(result)