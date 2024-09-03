class info:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

n = int(input())
info_list = []

for _ in range(n):
    inform = input().split()
    info1 = info(inform[0], int(inform[1]), int(inform[2]), int(inform[3]))
    info_list.append(info1)

info_list.sort(key = lambda x: x.score1 + x.score2 + x.score3)

for elem in info_list:
    print(elem.name, elem.score1, elem.score2, elem.score3)