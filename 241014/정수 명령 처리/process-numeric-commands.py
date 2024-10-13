class Stack():
    def __init__(self):
        self.s = []
    def push(self, A):
        self.s.append(A)
    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is empty")
        return self.s.pop()
    def size(self):
        return len(self.s)
    def empty(self):
        if not self.s:
            return 1
        else:
            return 0
    def top(self):
        return self.s[-1]

stack = Stack()

N = int(input())

for _ in range(N):
    order = tuple(input().split())
    if order[0] == 'push':
        stack.push(int(order[1]))
    elif order[0] == 'size':
        print(stack.size())
    elif order[0] == 'empty':
        print(stack.empty())
    elif order[0] == 'pop':
        print(stack.pop())
    elif order[0] == 'top':
        print(stack.top())