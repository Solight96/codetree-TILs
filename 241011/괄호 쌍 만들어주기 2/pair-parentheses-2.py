A = list(input())
cnt_i = 0
cnt_j = 0

num = 0

for i in range(len(A)-3):
    if A[i] == '(' and A[i+1] =='(':
        for j in range(i+2, len(A)-1):
            if A[j] == ')' and A[j+1] == ')':
                num += 1

print(num)