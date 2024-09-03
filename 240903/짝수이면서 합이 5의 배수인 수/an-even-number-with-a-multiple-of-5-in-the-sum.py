def chk(n):
    if n%2 == 0 and (n//10 + n%10)%5 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())

result = print(chk(n))