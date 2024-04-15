a, b = map(int, input().split())

def minab(a,b):
    if a>b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2

    return a, b

print(minab(a,b)[0], minab(a,b)[1], end=' ')