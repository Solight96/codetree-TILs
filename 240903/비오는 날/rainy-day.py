class info:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

info_list = []

for _ in range(n):
    information = tuple(input().split())
    info_list.append(information)
info_list.sort()

for i in range(n):
    if info_list[i][2] == 'Rain':
        print(*info_list[i])
        break