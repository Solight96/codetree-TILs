n, m = map(int, input().split())

v = [list(map(int, input().split())) for _ in range(n)]

def happyseq(row, col, m):
    cnt_r = 1
    cnt_c = 1
    num = 0

    r=[]
    c=[]
    
    if m == 1:
        return 2*n

    for i in range(row-1):
        for j in range(col-1):
            if v[i][j] == v[i][j+1]:
                cnt_r += 1
                if cnt_r >= m:
                    if not i in r:
                        r.append(i)
                        num += 1
            else:
                cnt_r = 1
            
            if v[i][j] == v[i+1][j]:
                cnt_c += 1
                if cnt_c >= m:
                    if not j in c:
                        c.append(j)
                        num += 1
            else:
                cnt_c = 1     
            
    return num

result = 0
result += happyseq(n, n, m)

print(result)