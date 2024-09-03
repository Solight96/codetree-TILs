class info:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

arr= []

for _ in range(5):
    information = input().split()
    information = (information[0], int(information[1]))
    arr.append(information)

idx = 0
score = arr[0][1]

for i in range(4):
    if arr[idx][1] > arr[i+1][1]:
        idx = i+1
        score = arr[i+1][1]

print(*arr[idx])