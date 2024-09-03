class info:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n

N = int(input())
info_list = []

for i in range(1, N+1):
    inform = input().split()
    info1 = info(int(inform[0]), int(inform[1]), i)
    info_list.append(info1)

info_list.sort(key = lambda x: (x.h, -x.w))

for elem in info_list:
    print(elem.h, elem.w, elem.n)