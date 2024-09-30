K, N = map(int, input().split())

ans = []

def print_ans():
    for elem in ans:
        print(elem, end=" ")
    print()

def make_ans(num):
    if num == N+1:
        print_ans()
        return
    
    for i in range(1, K+1):
        ans.append(i)
        make_ans(num + 1)
        ans.pop()
    
    return

make_ans(1)