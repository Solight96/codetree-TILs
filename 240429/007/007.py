class code:
    def __init__(self, secret_code, location, time):
        self.secret_code = secret_code
        self.location = location
        self.time = time
    

secret_code, location, time = map(str, input().split())
code1 = code(secret_code, location, time)
print(f"secret code : {code1.secret_code}")
print(f"meeting point : {code1.location}")
print(f"time : {code1.time}")