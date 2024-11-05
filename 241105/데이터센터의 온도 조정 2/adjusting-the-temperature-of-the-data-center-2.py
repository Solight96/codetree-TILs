N, C, G, H = map(int, input().split())

def work(Temp, a, b):
    if Temp < a:
        return C
    elif a <= Temp <= b:
        return G
    elif b < Temp:
        return H

arr = []

for _ in range(N):
    Ta, Tb = map(int, input().split())
    arr.append((Ta, Tb))

total = []

for i in range(min(min(arr))-10, max(max(arr))+10):
    result = 0
    for j in range(len(arr)):
        a, b = arr[j]
        w = work(i, a, b)
        result += w
    
    total.append(result)

print(max(total))