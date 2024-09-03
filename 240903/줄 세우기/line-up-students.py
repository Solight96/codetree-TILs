class info:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

N = int(input())
info_list = []

for i in range(1, N+1):
    inform = input().split()
    info1 = info(int(inform[0]), int(inform[1]), i)
    info_list.append(info1)

info_list.sort(key = lambda x: (-x.height, -x.weight, x.number))

for elem in info_list:
    print(elem.height, elem.weight, elem.number)