import copy

N, M, K = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(N)]
v2 = [[0] * N for _ in range(N)]
v3 = [[0] * N for _ in range(N)]

for k in range(K):
    for j in range(N):
        cnt = 1
        for i in range(N):
            if i == N-1:
                if cnt >= M:
                    for b in range(i-cnt+1, i+1):
                        v[b][j] = 0

            elif v[i][j] == v[i+1][j]:
                cnt += 1

            else:
                if cnt >= M:
                    for b in range(i-cnt+1, i+1):
                        v[b][j] = 0
                cnt = 1
    #폭탄터지기 완료
    
    for j in range(N):
        cnt = N-1
        for i in range(N-1, -1, -1):
            if v[i][j] != 0:
                v2[cnt][j] = v[i][j]
                cnt -= 1
    # 중력작용 완료

    for i in range(N-1, -1, -1):
        cnt = N-1
        for j in range(N-1, -1, -1):
            if v2[i][j] != 0:
                v3[cnt][(N-1)-i] = v2[i][j]
                cnt -= 1
    # 90도 회전 완료

    v = copy.deepcopy(v3)
    v2 = [[0] * N for _ in range(N)]
    v3 = [[0] * N for _ in range(N)]

for j in range(N):
    cnt = 1
    for i in range(N):
        if i == N-1:
            if cnt >= M:
                for b in range(i-cnt+1, i+1):
                    v[b][j] = 0

        elif v[i][j] == v[i+1][j]:
            cnt += 1

        else:
            if cnt >= M:
                for b in range(i-cnt+1, i+1):
                    v[b][j] = 0
            cnt = 1

if M == 1:
    num = 0

else:
    num = 0

    for i in range(N):
        for j in range(N):
            if v[i][j] != 0:
                num += 1

print(num)