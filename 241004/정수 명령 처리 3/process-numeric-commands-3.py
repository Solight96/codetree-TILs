from collections import deque

class Deque():
    def __init__(self):
        self.dq = deque()
    def push_front(self,num):
        self.dq.appendleft(num)
    def push_back(self,num):
        self.dq.append(num)
    def pop_front(self):
        return self.dq.popleft()
    def pop_back(self):
        return self.dq.pop()
    def size(self):
        return len(self.dq)
    def empty(self):
        if not dq: return 1
        else: return 0
    def front(self):
        return self.dq[0]
    def back(self):
        return self.dq[-1]

N = int(input())

dq = Deque()

for _ in range(N):
    order = tuple(input().split())
    if order[0] == 'push_back':
        dq.push_back(int(order[1]))
    elif order[0] == 'push_front':
        dq.push_front(int(order[1]))
    elif order[0] == 'pop_front':
        print(dq.pop_front())
    elif order[0] == 'pop_back':
        print(dq.pop_back())
    elif order[0] == 'size':
        print(dq.size())
    elif order[0] == 'empty':
        print(dq.empty())
    elif order[0] == 'front':
        print(dq.front())
    elif order[0] == 'back':
        print(dq.back())