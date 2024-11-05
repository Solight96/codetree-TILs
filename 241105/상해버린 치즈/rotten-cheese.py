N, M, D, S = map(int, input().split())
# N: 사람 수 / M: 치즈 수 / D : '누가 치즈 먹었니' 수 / S : '언제 아팠니' 수 

arr_d = []
arr_s = []

for i in range(D):
    arr_d.append(list(map(int, input().split()))) # p(누가), m(어떤 치즈를), t(언제 먹었니)

for j in range(S):
    arr_s.append(list(map(int, input().split()))) # p(누가), t(언제 아팠니)

arr_pmt = []

for m in range(S):
    for n in range(D):
        if arr_s[m][0] == arr_d[n][0] and arr_s[m][1] > arr_d[n][2]: # 치즈를 먹고나서 아프게 됐으면
            arr_pmt.append(arr_d[n]) # 그 때의 pmt를 저장 (아프기 전에 먹었던 치즈 정보 확보)

arr_m = []

if len(arr_pmt) != 1 and S != 1: # 아픈 사람이 여러 명이면
    for i in range(len(arr_pmt)):
        for j in range(len(arr_pmt)):
            if i == j:
                continue
            if arr_pmt[i][1] == arr_pmt[j][1]: # 같은 치즈를 먹었으면
                if not arr_pmt[j][1] in arr_m:
                    arr_m.append(arr_pmt[j][1]) # 그 때의 m을 저장 (같이 먹었기에 의심되는 치즈..)
else: # 아픈 사람이 혼자면
    arr_m = [arr_pmt[0][1]]

arr = []

for i in range(len(arr_m)):
    arr_p = []
    for j in range(D):
        if arr_m[i] == arr_d[j][1]: # 의심되는 치즈를 먹은 사람
            if not arr_d[j][0] in arr_p:
                arr_p.append(arr_d[j][0])
    arr.append(len(arr_p))

print(max(arr))