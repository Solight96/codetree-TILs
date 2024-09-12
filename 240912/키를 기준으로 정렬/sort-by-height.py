class info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
info_list= []

for _ in range(n):
    information = input().split()
    info1 = info(information[0], information[1], information[2])
    info_list.append(info1)

info_list.sort(key = lambda x : x.height)

for elem in info_list:
    print(elem.name, elem.height, elem.weight)