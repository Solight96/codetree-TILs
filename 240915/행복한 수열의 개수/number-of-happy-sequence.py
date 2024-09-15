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

    for i in range(row):
        for j in range(col):
            if j+1 < col and v[i][j] == v[i][j+1]:
                cnt_r += 1
                if cnt_r >= m:
                    if not i in r:
                        r.append(i)
                        num += 1
            else:
                cnt_r = 1
            
            if i+1 < row and v[i][j] == v[i+1][j]:
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