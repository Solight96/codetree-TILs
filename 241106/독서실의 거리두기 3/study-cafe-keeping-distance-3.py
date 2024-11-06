N = int(input())

arr = list(input())

result = 0
x, y = 0, 0

for i in range(len(arr)-1):
    cnt = 0
    if arr[i] == '1':
        for j in range(i+1, len(arr)):
            if not arr[j] == '1':
                cnt += 1
            else:
                cnt += 1
                break
                
    if result < cnt:
        result = cnt
        x = i
        y = j

arr[(x+y)//2] = '1'

result2 = 1000000

for i in range(len(arr)-1):
    if arr[i] == '1':
        cnt = 0
        for j in range(i+1, len(arr)):
            if not arr[j] == '1':
                cnt += 1
            else:
                cnt += 1
                break
    
    if result2 > cnt:
        result2 = cnt

print(result2)

# print(min(abs(x-(x+y)//2), abs(y-(x+y)//2)))