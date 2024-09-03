class info:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

information = tuple(input().split())

info1 = info(information[0], information[1], information[2])

print(f"code : {info1.code}")
print(f"color : {info1.color}")
print(f"second : {info1.time}")