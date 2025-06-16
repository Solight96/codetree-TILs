A = input()

A_list = list(A)
B_list = list(reversed(A_list))

if A_list == B_list:
    print("Yes")
else:
    print("No")