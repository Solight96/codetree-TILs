str1 = str(input())
str2 = str(input())

arr1 = []
arr2 = []

for i in range(len(str1)):
    if ord(str1[i]) >= 48 and ord(str1[i]) <= 57:
        arr1.append(str1[i])

for i in range(len(str2)):
    if ord(str2[i]) >= 48 and ord(str2[i]) <= 57:
        arr2.append(str2[i])

result1 = int(''.join(arr1))
result2 = int(''.join(arr2))

result = result1 + result2
print(result)