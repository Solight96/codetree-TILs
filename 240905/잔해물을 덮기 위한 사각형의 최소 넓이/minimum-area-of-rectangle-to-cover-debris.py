ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())


if ax1 < bx1:
    if ay1 > by1 and ay2 < by2:
        print((bx1 - ax1) * (ay2 - ay1))
    else:
        print((ax2 - ax1) * (ay2 - ay1))

elif bx1 < ax1:
    if ay1 > by1 and ay2 < by2:
        print((ax2 - bx2) * (ay2 - ay1))  
    else:
        print((ax2 - ax1) * (ay2 - ay1))