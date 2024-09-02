a1, a2 = map(int, input().split())

result=[]
result.append(a1)
result.append(a2)

for i in range(2, 10):
    result.append(result[i-1]+2*result[i-2])

print(*result)