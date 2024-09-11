n = int(input())

elem = list(map(int, input().split()))

elem.sort()
print(*elem)

elem.sort(reverse=True)
print(*elem)