class info:
    def __init__(self, name, code):
        self.name = name
        self.code = code

information = tuple(input().split())

info1 = info("codetree", "50")
info2 = info(information[0], information[1])

print(f"product {info1.code} is {info1.name}")
print(f"product {info2.code} is {info2.name}")