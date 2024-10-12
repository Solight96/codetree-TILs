N, K = map(int, input().split())

arr = []
GH = [0] * 10000

for _ in range(N):
    loc, alpha = input().split()
    arr.append(int(loc))
    GH[int(loc)-1] = alpha

max_val = max(arr)
result = 0

for i in range(max_val-K+1):
    num = 0
    for j in range(i, i+K+1):
        if GH[j] == 'G':
            num += 1
        elif GH[j] == 'H':
            num += 2
    
    if result < num:
        result = num

print(result)