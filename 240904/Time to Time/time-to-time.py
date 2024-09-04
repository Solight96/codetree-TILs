def time(a,b):
    hour = 0
    minute = 0
    cnt = 0

    while True:
        if hour == a and minute == b:
            break
        if minute == 60:
            hour += 1
            minute = 0
        minute += 1
        cnt += 1
    return cnt


a, b, c, d = map(int, input().split())

time1 = time(a, b)
time2 = time(c, d)
print(time2 - time1)