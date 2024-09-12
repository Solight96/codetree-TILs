class inform:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = []

for _ in range(n):
    information = tuple(input().split())
    info = inform(information[0], int(information[1]), int(information[2]))
    arr.append(info)

arr.sort(key = lambda x: (x.height, -x.weight))

for elem in arr:
    print(elem.name, elem.height, elem.weight)