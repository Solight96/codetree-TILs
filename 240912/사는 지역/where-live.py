class info:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

n = int(input())

info_list = []

for _ in range(n):
    information = tuple(input().split())
    info_list.append(information)
info_list.sort()

print(f"name {info_list[-1][0]}")
print(f"addr {info_list[-1][1]}")
print(f"city {info_list[-1][2]}")