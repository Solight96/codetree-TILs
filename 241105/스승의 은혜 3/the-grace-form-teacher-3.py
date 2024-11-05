import copy

N, B = map(int, input().split())
arr = []
student = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    cnt = 0
    arr2 = copy.deepcopy(arr)
    arr2[i][0] //= 2
    arr2.sort(key=lambda x: x[0]+x[1])
    
    for j in range(len(arr2)):
        B -= (arr2[j][0] + arr2[j][1])
        if B >= 0:
            cnt += 1
        else:
            student.append(cnt)
            break

print(max(student))