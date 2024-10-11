N = int(input())

height = list(map(int, input().split()))
num = 0

for i in range(len(height)):
    for j in range(i+1, len(height)):
        if height[i] <= height[j]:
            for k in range(j+1, len(height)):
                if height[j] <= height[k]:
                    num += 1

print(num)