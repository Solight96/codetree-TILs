class info:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

n = int(input())

for _ in range(n):
    information = [tuple(input().split())]
    information.sort()

print(f"name {information[-1][0]}")
print(f"addr {information[-1][1]}")
print(f"city {information[-1][2]}")