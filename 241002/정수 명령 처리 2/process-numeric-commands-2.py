from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()
    def push(self, item):
        self.dq.append(item)
    def empty(self):
        if self.dq:
            return 0
        else: 
            return 1
    def size(self):
        return len(self.dq)
    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq.popleft()
    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq[0]


N = int(input())
q = Queue()

for _ in range(N):
    order = tuple(input().split())
    if order[0] == 'push':
        q.push(order[1])
    elif order[0] == 'pop':
        print(q.pop())
    elif order[0] == 'size':
        print(q.size())
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'front':
        print(q.front())