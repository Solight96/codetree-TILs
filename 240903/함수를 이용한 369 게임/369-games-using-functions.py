def check369(n):
    n = str(n)
    cnt = 0
    for i in range(len(n)):
        if n[i] == '3' or n[i] == '6' or n[i] == '9':
            cnt = 1
    return cnt

a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if check369(i) or i%3 == 0:
        cnt += 1

print(cnt)