def lcm(k):
    while k:
        if len(k)==1:
            return k[0]
        a = k.pop()
        b = k.pop()
        for i in range(max(a,b), a*b+1):
            if i%a==0 and i%b==0:
                k.append(i)
                break
        lcm(k)

n = int(input())
m = list(map(int, input().split()))

result = lcm(m)
print(result)