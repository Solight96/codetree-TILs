class distance:
    def __init__(self, m, n, i):
        self.m = m
        self.n = n
        self.i = i

N = int(input())
arr = []

for i in range(1, N+1):
    point = tuple(map(int, input().split()))
    dist = distance(point[0], point[1], i)
    arr.append(dist)

arr.sort(key = lambda x: abs(x.m)+abs(x.n))

for elem in arr:
    print(elem.i)