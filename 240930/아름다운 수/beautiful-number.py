n = int(input())

ans = []

def chk_beaunum():
    cnt = 1

    for i in range(len(ans)):
        if i == len(ans)-1:
            if cnt == 1:
                if ans[i] == 1:
                    return True
                else:
                    return False
            else:
                if cnt%ans[i] == 0:
                    return True
                else:
                    return False

        elif ans[i] != ans[i+1]:
            if cnt%ans[i] == 0:
                cnt = 1
                continue
            else:
                return False
        else:
            cnt += 1

# global result
# result = 0

def find_result(num, result):
    if num == n+1:
        is_beau = chk_beaunum()
        if is_beau:
            result += 1
        return result
    
    for i in range(1, 5):
        ans.append(i)
        result = find_result(num+1, result)
        ans.pop()

    return result


result = find_result(1, 0)
print(result)