n = int(input())

def star_p(n):
    if n<=0:
        return
    print('* '*n)
    star_p(n-1)
    print('* '*n)

star_p(n)