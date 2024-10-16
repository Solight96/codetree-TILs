n, m = map(int, input().split())
arr = [[[int(num)] for num in input().split()] for _ in range(n)]

move_arr = list(map(int, input().split()))

dxs = [-1, 0, 1, 0, -1, 1, 1, -1]
dys = [0, 1, 0, -1, 1, 1, -1, -1]

# 격자 내에 있는지 체크
def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

# 숫자 이동하기
def move_cur_num(a, b, c, cur_num, max_row, max_col, tar_idx, max_num, move_num) :
    temp_arr = []

    if max_num != 0:
        for e in arr[a][b][:move_num + 1]:
            temp_arr.append(e)
            arr[a][b].remove(e)

    for e in arr[max_row][max_col] :
        temp_arr.append(e)

    arr[max_row][max_col] = temp_arr

    if len(arr[a][b]) == 0 :
        arr[a][b].append(0)
    
    return arr


# 8방향 중에서 가장 큰 수가 있는지 체크
def find_the_biggest_num(row, col, point) :
    max_num = -1
    tar_idx = -1
    
    for dx, dy in zip(dxs, dys) :
        next_row = row + dx
        next_col = col + dy

        if in_range(next_row, next_col) :
            for e in arr[next_row][next_col] :
                if e >= max_num :
                    max_num = e
                    max_row = next_row
                    max_col = next_col
                    tar_idx = arr[next_row][next_col].index(e)
    return max_row, max_col, tar_idx, max_num
    print(row, col, point, max_num, tar_idx)

# 움직일 숫자의 위치 찾기
def find_loc(arr, num) :
    for a in range(len(arr)) :
        for b in range(len(arr[a])) :
            for c in range(len(arr[a][b])) :
                if arr[a][b][c] == num :
                    return a, b, c

for i in range(len(move_arr)) :
    a, b, c = find_loc(arr, move_arr[i])
    max_row, max_col, tar_idx, max_num = find_the_biggest_num(a, b, c) 
    arr = move_cur_num(a, b, c, arr[a][b][c], max_row, max_col, tar_idx, max_num, move_arr[i])

for e in arr :
    for ee in e :
        for eee in ee :
            if eee == 0 :
                print('None', end = ' ')
            else :
                print(eee, end = ' ')
        print()