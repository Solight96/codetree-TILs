A = input()

def alpha2(a):
    a = set(list(a))
    if len(a) >= 2:
        print("Yes")
    else:
        print("No")

alpha2(A)