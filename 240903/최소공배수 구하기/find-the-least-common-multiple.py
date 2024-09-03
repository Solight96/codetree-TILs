n,m = map(int, input().split())

def lcm(a,b):
    k = 0
    for i in range(max(a,b), a*b+1, 1):
        if i%a ==0 and i%b ==0:
            k = i
            break
    return k

print(lcm(n,m))