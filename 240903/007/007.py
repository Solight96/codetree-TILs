class info:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

infomation = input().split()

info1 = info(infomation[0], infomation[1], infomation[2])

print(f"secret code : {info1.code}")
print(f"meeting point : {info1.location}")
print(f"time : {info1.time}")