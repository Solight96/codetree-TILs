N, M, D, S = map(int, input().split())
# N: 사람 수 / M: 치즈 수 / D : '누가 치즈 먹었니' 수 / S : '언제 아팠니' 수 

arr_d = []
arr_s = []

for i in range(D):
    arr_d.append(list(map(int, input().split()))) # p(누가), m(어떤 치즈를), t(언제 먹었니)

for j in range(S):
    arr_s.append(list(map(int, input().split()))) # p(누가), t(언제 아팠니)

arr_pmt = []
arr_people = []

for m in range(S):
    for n in range(D):
        if arr_s[m][0] == arr_d[n][0] and arr_s[m][1] > arr_d[n][2]: # 치즈를 먹고나서 아프게 됐으면
            arr_pmt.append(arr_d[n]) # 그 때의 pmt를 저장 (아프기 전에 먹었던 치즈 정보 확보)
            arr_people.append(arr_d[n][0])
arr_pmt.sort()
num_people = len(set(arr_people))

arr_m = [[] for _ in range(N+1)]
arr_m2 = []

for i in range(len(arr_pmt)):
    p,m,t = arr_pmt[i]
    arr_m[p].append(m)

for i in range(M):
    cnt = 0
    for j in range(len(arr_m)):
        if i in arr_m[j]:
            cnt += 1
    if cnt == num_people:
        arr_m2.append(i)

arr = []

for i in range(len(arr_m2)):
    arr_p = []
    for j in range(D):
        if arr_m2[i] == arr_d[j][1]: # 의심되는 치즈를 먹은 사람
            if not arr_d[j][0] in arr_p:
                arr_p.append(arr_d[j][0])
    arr.append(len(arr_p))

print(max(arr))