from collections import deque

class Deque():
    def __init__(self):
        self.dq = deque()
    def push_front(self,num):
        self.dq.appendleft(num)
    def push_back(self,num):
        self.dq.append(num)
    def pop_front(self):
        print(self.dq.popleft())
    def pop_back(self):
        print(self.dq.pop())
    def size(self):
        print(len(self.dq))
    def empty(self):
        if self.dq: print(0)
        else: print(1)
    def front(self):
        print(self.dq[0])
    def back(self):
        print(self.dq[-1])

N = int(input())

dq = Deque()

for _ in range(N):
    order = tuple(input().split())
    if order[0] == 'push_back':
        dq.push_back(int(order[1]))
    elif order[0] == 'push_front':
        dq.push_front(int(order[1]))
    elif order[0] == 'pop_front':
        dq.pop_front()
    elif order[0] == 'pop_back':
        dq.pop_back()
    elif order[0] == 'size':
        dq.size()
    elif order[0] == 'empty':
        dq.empty()
    elif order[0] == 'front':
        dq.front()
    elif order[0] == 'back':
        dq.back()