T, a, b = map(int,input().split())

arr = [0] * 1001

for _ in range(T):
    c, x = input().split()
    arr[int(x)] = c

result = []

for i in range(a, b+1):
    d1_list = []
    d2_list = []
    for j in range(a, b+1):
        if arr[j] == 'S':
            d1_list.append(abs(j-i))
            d1 = min(d1_list)
    for j in range(a, b+1):
        if arr[j] == 'N':
            d2_list.append(abs(j-i))
            d2 = min(d2_list)
    
    if d1 <= d2:
        result.append(i)

print(len(result))