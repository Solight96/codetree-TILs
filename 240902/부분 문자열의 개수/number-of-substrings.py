A = str(input())
B = str(input())

cnt = 0

for i in range(len(A)-1):
    if (A[i]+A[i+1]) == B:
        cnt += 1
print(cnt)