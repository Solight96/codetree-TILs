class number:
    def __init__(self, num, i):
        self.num = num
        self.i = i

N = int(input())

nums = tuple(map(int, input().split()))
arr = []
arr2 = []

for i in range(1, N+1):
    num = number(nums[i-1], i)
    arr.append(num)

arr.sort(key = lambda x: x.num)

for elem in arr:
    arr2.append(elem.i)

for i in range(1, N+1):
    print(arr2.index(i)+1, end = ' ')