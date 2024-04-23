N = int(input())

array = []

for _ in range(N):
    order = str(input())
    if ' ' in order:
        order, num = order.split(' ')
    if order == 'push_back':
        array.append(int(num))
    elif order == 'pop_back':
        array.pop()
    elif order == 'size':
        print(len(array))
    elif order == 'get':
        print(array[int(num) - 1])