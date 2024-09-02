string = str(input())
string_list = list(string)

for i in range(1, len(string)):
    if string[i] == string[1]:
        string_list[i] = string_list[0]

result = ''.join(string_list)

print(result)