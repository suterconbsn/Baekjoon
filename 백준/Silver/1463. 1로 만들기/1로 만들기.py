dy=[0] * 1000001
import sys
n=int(sys.stdin.readline().rstrip())

def filter(n, b=0):
    if dy[n] != 0:
        return dy[n]

    if n ==1:
        return 0

    else:
        a=[]
        if n%3==0:
            a.append(filter(n // 3, 0) + 1)
        if n%2==0:
            a.append(filter(n // 2, 0) + 1)
        if b<6:
            a.append(filter(n-1, b+1) + 1)
            dy[n] = min(a)
            return dy[n]
        return n


print(filter(n))
