from collections import deque
import sys

class Stack:
    def __init__(self, maxlen):
        self.capacity = maxlen
        self.__stk = deque([], maxlen)
    def push(self, value):
        self.__stk.append(value)
    def pop(self):
        return self.__stk.pop()
    def is_empty(self):
        return not self.__stk
    def __len__(self):
        return len(self.__stk)
    def peek(self):
        return self.__stk[-1]
    def clear(self):
        self.__stk.clear()

n=int(sys.stdin.readline().rstrip())

a=Stack(10000)
for i in range(n):
    order=sys.stdin.readline().split()
    if order[0] == 'push':
        a.push(order[1])
    elif order[0] == 'pop':
        if a.is_empty():
            print('-1')
            continue
        print(a.pop())
    elif order[0] == 'size':
        print(len(a))
    elif order[0] == 'empty':
        if a.is_empty():
            print('1')
        else:
            print('0')
    elif order[0] == 'top':
        if a.is_empty():
            print('-1')
            continue
        print(a.peek())