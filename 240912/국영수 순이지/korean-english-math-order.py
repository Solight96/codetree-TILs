class info:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat 

n = int(input())
info_list = []

for _ in range(n):
    
    inform = input().split()
    info1 = info(inform[0], int(inform[1]), int(inform[2]), int(inform[3]))
    info_list.append(info1)

info_list.sort(key= lambda x: (-x.kor, -x.eng, -x.mat))

for elem in info_list:
    print(elem.name, elem.kor, elem.eng, elem.mat)