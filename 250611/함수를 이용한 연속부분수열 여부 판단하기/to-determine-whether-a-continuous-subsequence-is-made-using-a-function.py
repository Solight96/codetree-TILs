n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_conti_partial_seq(a, b):
    q = b[0]

    for i in range(len(a)):
        if i+len(b) > len(a): return False
        if a[i] == q:
            s = 1
            for j in range(i, i+len(b)):
                if a[j] != b[j-i]:
                    s = 0
                    break
            if s: return True

if is_conti_partial_seq(a,b):
    print("Yes")
else:
    print("No")