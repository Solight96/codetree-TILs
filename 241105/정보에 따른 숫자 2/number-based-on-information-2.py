import sys

T, a, b = map(int,input().split())

arr = [0] * 1001

for _ in range(T):
    c, x = input().split()
    arr[int(x)] = c

result = []

for i in range(a, b+1):
    d1_list = []
    d2_list = []
    d1 = sys.maxsize
    d2 = sys.maxsize
    
    for j in range(b+1):
        if arr[j] == 'S':
            d1_list.append(abs(j-i))
    if len(d1_list) != 0:
        d1 = min(d1_list)
    # print(f"[{i}] d1={d1}")
    
    for j in range(b+1):
        if arr[j] == 'N':
            d2_list.append(abs(j-i))
    if len(d2_list) != 0:
        d2 = min(d2_list)
    # print(f"[{i}] d2={d2}")
    
    if d1 <= d2:
        result.append(i)

print(len(result))