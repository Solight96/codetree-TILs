class info:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

n = int(input())
arr1 = []
arr2 = []
arr3 = []
idx = 0

for _ in range(n):
    inforamtion = tuple(input().split())
    arr1.append(inforamtion[0])
    arr2.append(inforamtion[1])
    arr3.append(inforamtion[2])

for i in range(n-1):
    if arr1[i][0] < arr1[i+1][0]:
        idx = i+1

print(f"name {arr1[idx]}")
print(f"addr {arr2[idx]}")
print(f"city {arr3[idx]}")