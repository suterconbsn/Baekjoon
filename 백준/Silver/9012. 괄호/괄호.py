from collections import deque

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
    def clear(self):
        self.__stk.clear()

def saveVPS(a, VPS):
    for j in VPS:
        if j == ')':
            if a.is_empty():
                return 'NO'
            a.pop()
        elif j == '(':
            a.push(j)
    if a.is_empty():
        return 'YES'
    else:
        a.clear()
        return 'NO'


n=int(input())

a = Stack(50)

for i in range(n):
    VPS=list(input().replace(" ", ""))
    print(saveVPS(a, VPS))


