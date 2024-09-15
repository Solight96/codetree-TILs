n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]

num = 0

# 가로
for i in range(n):
    number = v[i][0]
    cnt = 0

     # 갯수에 자기 자신이 포함되므로 자기 자신과 비교할 때부터 1이 카운트 된다
    for j in range(n):
        if number == v[i][j]:
            cnt += 1
        else:
           # 다음 숫자와 비교하기 위해 number 에 넣어준다
            number = v[i][j]
            cnt = 1
        if cnt == m:
            num += 1
            cnt = 1
            break
        
# 세로
for j in range(n):
    number = v[0][j]
    cnt = 0

    # 갯수에 자기 자신이 포함되므로 자기 자신과 비교할 때부터 1이 카운트 된다
    for i in range(n):
        if number == v[i][j]:
            cnt += 1
        else:
            # 다음 숫자와 비교하기 위해 number 에 넣어준다
            number = v[i][j]
            cnt = 1
        if cnt == m:
            num += 1
            cnt = 1
            break

print(num)