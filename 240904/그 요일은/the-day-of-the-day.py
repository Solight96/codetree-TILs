day_arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_arr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def time(m1, d1, m2, d2, date):
    cnt = 0
    while True:
        if m2 == m1:
            break
        m2 -= 1
        d2 += day_arr[m2]
    cnt += d2 - d1

    if cnt%7 < date_arr.index(date):
        return cnt//7 
    else:
        return cnt//7 + 1

m1, d1, m2, d2 = map(int, input().split())
date = input()

result = time(m1, d1, m2, d2, date)

print(result)