A, B, x, y = map(int, input().split())

d1 = abs(A-B)
d2 = abs(A-x) + abs(y-B)
d3 = abs(A-y) + abs(x-B)

print(min(d1, d2, d3))