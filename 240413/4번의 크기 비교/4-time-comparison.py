a = int(input())
b,c,d,e = map(int, input().split())

com_list = [b,c,d,e]

for element in com_list:
    if a>element:
        print(1)
    else:
        print(0)