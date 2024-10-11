n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr10000 = [elem // 10000 for elem in arr]
arr1000 = [(elem % 10000) // 1000 for elem in arr]
arr100 = [(elem % 1000) // 100 for elem in arr]
arr10 = [(elem % 100) // 10 for elem in arr]
arr1 = [elem % 10 for elem in arr]

result = -1

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            if arr1000[i] + arr1000[j] + arr1000[k] < 10 and arr100[i] + arr100[j] + arr100[k] < 10 and arr10[i] + arr10[j] + arr10[k] < 10 and arr1[i] + arr1[j] + arr1[k] < 10:
                num = arr[i] + arr[j] + arr[k]
                if result < num:
                    result = num

print(result)