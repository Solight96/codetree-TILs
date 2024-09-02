n = int(input())

add = 0

for _ in range(n):
    num = int(input())

    add += num

string = str(add)
string = string[1:] + string[0]

print(string)