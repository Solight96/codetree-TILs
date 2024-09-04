days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day(a, b):
    month = 1
    date = 1
    cnt = 0

    while True:
        if month == a and date == b:
            break
        
        date += 1
        cnt += 1
        
        if date > days[month]:
            month += 1
            date = 1

    return cnt

m1, d1, m2, d2 = map(int, input().split())

day1 = day(m1, d1)
day2 = day(m2, d2)

print(day2 - day1 + 1)