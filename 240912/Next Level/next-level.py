class character:
    def __init__(self, identity=None, level=None):
        self.identity = identity
        self.level = level

ch1 = character()
ch2 = character()

ch1.identity = 'codetree'
ch1.level = 10

a, b = input().split()

ch2.identity = a
ch2.level = int(b)

print(f"user {ch1.identity} lv {ch1.level}")
print(f"user {ch2.identity} lv {ch2.level}")