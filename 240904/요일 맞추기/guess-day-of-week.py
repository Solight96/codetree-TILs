day_arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_arr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def date(m1, d1, m2, d2):
    cnt = 0
    while True:
        if m2 == m1:
            break
        if m2 > m1:
            m2 -= 1
            d2 += day_arr[m2]
        else:
            m1 -= 1
            m1 += day_arr[m1]
    
    cnt += abs(d2 - d1)

    return date_arr[cnt%7]

m1, d1, m2, d2 = map(int, input().split())

result = date(m1, d1, m2, d2)

print(result)