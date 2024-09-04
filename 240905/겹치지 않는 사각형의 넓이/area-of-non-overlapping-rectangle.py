ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

v = [[0] * 2000 for _ in range(2000)]
result = 0

for i in range(ax1, ax2):
    for j in range(ay1, ay2):
        v[i][j] = 1

for i in range(bx1, bx2):
    for j in range(by1, by2):
        v[i][j] = 2
for i in range(mx1, mx2):
    for j in range(my1, my2):
        v[i][j] = 3

for elem in v:
    result += elem.count(1) 
    result += elem.count(2) 

print(result)