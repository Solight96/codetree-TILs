A = list(input())

def RLE(word):
    result = word[0]
    cnt = 1
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            cnt += 1
        else:
            result += str(cnt)
            result += word[i]
            cnt = 1
    result += str(cnt)

    return len(result)

length = RLE(A)

for _ in range(len(A)):
    temp = A[-1]
    for i in range(len(A)-1, 0, -1):
        A[i] = A[i-1]
    A[0] = temp

    if length >= RLE(A):
        length = RLE(A)

print(length)