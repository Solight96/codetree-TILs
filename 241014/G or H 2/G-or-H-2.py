N = int(input())

arr = [0] * 101
arr2 = []

for _ in range(N):
    inform = tuple(input().split())
    arr[int(inform[0])] = inform[1]
    arr2.append(int(inform[0]))

result = []
arr = arr[:max(arr2)+1]

for i in range(len(arr)):
    for j in range(len(arr)-i):
        cnt_G = 0
        cnt_H = 0
        arr2 = []
        for k in range(j, j+i+1):
            if arr[k] == 'G':
                cnt_G += 1
                arr2.append(k)
                # print(f"j={j}, k={k}, cnt_G={cnt_G}")
            elif arr[k] == 'H':
                cnt_H += 1
                arr2.append(k)
                # print(f"j={j}, k={k}, cnt_H={cnt_H}")

        if (cnt_G * cnt_H == 0 and cnt_G + cnt_H != 0) or (cnt_G * cnt_H != 0 and cnt_G == cnt_H):
            arr2.sort()
            dist = arr2[-1] - arr2[0]
            result = dist

    # print(f"---------------i={i}")

if N == 1:
    print(0)
else:
    print(result)