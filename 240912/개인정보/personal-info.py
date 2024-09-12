class inform:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = []

for _ in range(5):
    information = list(input().split())
    info = inform(information[0], int(information[1]), float(information[2]))
    arr.append(info)

print("name")
arr.sort(key = lambda x: x.name)
for elem in arr:
    print(elem.name, elem.height, elem.weight)

print()

print("height")
arr.sort(key = lambda x: -x.height)
for elem in arr:
    print(elem.name, elem.height, elem.weight)