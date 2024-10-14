def cal(a,o,c):
    if o == '+':
        print(f"{a} {o} {c} = {int(a)+int(c)}")
    elif o == '-':
        print(f"{a} {o} {c} = {int(a)-int(c)}")
    elif o == '*':
        print(f"{a} {o} {c} = {int(a)*int(c)}")
    elif o == '/':
        print(f"{a} {o} {c} = {int(a)//int(c)}")
    else:
        print("False")

a, o, c = input().split()

cal(a,o,c)