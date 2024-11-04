N, M, D, S = map(int, input().split())
# N: 사람 수 / M: 치즈 수 / D : '누가 치즈 먹었니' 수 / S : '언제 아팠니' 수 

arr_d = []
arr_s = []
arr_pmt = []
arr_pmt2 = []
arr_p = []

for i in range(D):
    arr_d.append(list(map(int, input().split()))) # p(누가), m(어떤 치즈를), t(언제 먹었니)

for j in range(S):
    arr_s.append(list(map(int, input().split()))) # p(누가), t(언제 아팠니)

for m in range(S):
    for n in range(D):
        if arr_s[m][0] == arr_d[n][0] and arr_s[m][1] > arr_d[n][2]: # 치즈를 먹고나서 아프게 됐으면
            arr_pmt.append(arr_d[n]) # 그 때의 pmt를 저장

if len(arr_pmt) != 1 and S != 1: # 아픈 사람이 여러 명이면
    for i in range(len(arr_pmt)):
        for j in range(len(arr_pmt)):
            if i == j:
                continue
            if arr_pmt[i][1] == arr_pmt[j][1]: # 같은 치즈를 먹었으면
                arr_pmt2.append(arr_pmt[j]) # 그 때의 pmt를 저장
else: # 아픈 사람이 혼자면
    arr_pmt2 = arr_pmt

for i in range(len(arr_pmt2)):
    for j in range(D):
        if arr_pmt2[i][1] == arr_d[j][1] and arr_pmt2[i][2] <= arr_d[j][2]:
            arr_p.append(arr_d[j][0])

print(len(set(arr_p)))