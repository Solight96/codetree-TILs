n = int(input())

arr = list(input().split())

def sorting(alpha_list, alpha, loc, cnt = 0):
    idx = alpha_list.index(alpha)
    if idx == loc:
        if loc == len(alpha_list) - 1:
            print(cnt)
            return
        else:
            sorting(alpha_list, chr(ord(alpha)+1), loc+1, cnt)
    else:
        dist = abs(idx - loc)
        tmp = alpha_list.pop(idx)
        alpha_list.insert(loc, tmp)
        cnt += dist
        sorting(alpha_list, chr(ord(alpha)+1), loc+1, cnt)

sorting(arr, 'A', 0, 0)