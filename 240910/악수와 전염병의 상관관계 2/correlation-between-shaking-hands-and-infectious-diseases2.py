N, K, P, T = map(int, input().split())

arr_inform = []
arr_cnt = [0] * (N+1) # (전염된 이후의)악수 횟수
arr_inj = [0] * (N+1) # 감염 여부

arr_inj[P] = 1

for _ in range(T):
    inform = tuple(map(int, input().split()))
    arr_inform.append(inform)

arr_inform.sort()

for i in range(len(arr_inform)):
    if arr_inj[arr_inform[i][1]] == 0:
        if arr_inj[arr_inform[i][2]] == 0:
            continue
        else:
            if arr_cnt[arr_inform[i][2]] < K:
                arr_inj[arr_inform[i][1]] = 1
                arr_cnt[arr_inform[i][2]] += 1
            else:
                continue
    else:
        if arr_inj[arr_inform[i][2]] == 1:
            arr_cnt[arr_inform[i][1]] += 1
            arr_cnt[arr_inform[i][2]] += 1
        else:
            if arr_cnt[arr_inform[i][1]] < K:
                arr_inj[arr_inform[i][2]] = 1
                arr_cnt[arr_inform[i][1]] += 1
            else:
                continue

for i, elem in enumerate(arr_inj):
    if i >= 1:
        print(arr_inj[i], end='')