def is_date_exist(m, d):
    if m == 2 and 1 <= d <= 28: return True
    elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and 1 <= d <= 31: return True
    elif (m == 4 or m == 6 or m == 9 or m == 11) and 1 <= d <= 30: return True
    return False

M, D = map(int, input().split())

if is_date_exist(M, D): print("Yes")
else : print("No")