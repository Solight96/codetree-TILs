A = list(input())

num = 0

for i in range(len(A)):
    if A[i] == '(':
        for j in range(i+1, len(A)):
            if A[j] == ')':
                num += 1

print(num)