def time(a, b, c):
    day = 1
    hour = 0
    minute = 0

    cnt = 0

    while True:
        if day == a and hour == b and minute == c:
            break
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 24:
            day += 1
            hour = 0
        
        minute +=1
        cnt += 1

    return cnt

a, b, c = map(int, input().split())

time1 = time(11, 11, 11)
time2 = time(a, b, c)

if time2 < time1:
    print(-1)
else:
    print(time2 - time1)