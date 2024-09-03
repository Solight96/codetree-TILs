def year(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return False # 평년
        return True # 윤년
    else:
        return False # 평년

y = int(input())

if year(y):
    print("true")
else:
    print("false")