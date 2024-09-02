A = str(input())

order = str(input())

for i in range(len(order)):
    if order[i] == 'R':
        A = A[-1] + A[:-1]
    elif order[i] == 'L':
        A = A[1:] + A[0]
print(A)