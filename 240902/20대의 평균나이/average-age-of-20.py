result = []

while True:
    age = int(input())
    if age >= 20 and age<30:
        result.append(age)
    else:
        break

print("{:.2f}".format(sum(result) / len(result)))