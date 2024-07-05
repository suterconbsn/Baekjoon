import sys
from itertools import combinations

def plus123(n):
    total=1
    a=[1]*n
    if n>=2:
        c=0 
        if n%2==0:
            for i in range(len(a)-1, -1, -2):
                c+=1
                a[i-1] = a[i] + a[i-1]
                a.pop(i)
                total += len(list(combinations(a, c)))
        else:
            for i in range(len(a)-1, 0, -2):
                c += 1
                a[i-1] = a[i] + a[i-1]
                a.pop(i)
                total += len(list(combinations(a, c)))
    if n>=3: 
        a = [1] * n
        c=0
        if n%3==0:
            for i in range(len(a)-1, -1, -3):
                c+=1
                a[i-2] = a[i] + a[i-1] + a[i-2]
                a.pop(i)
                a.pop(i-1)
                total += len(list(combinations(a, c)))
        elif n%3==1:
            for i in range(len(a)-1, 0, -3):
                c+=1
                a[i-2] = a[i] + a[i-1] + a[i-2]
                a.pop(i)
                a.pop(i-1)
                total += len(list(combinations(a, c)))
        else:
            for i in range(len(a)-1, 1, -3):
                c+=1
                a[i-2] = a[i] + a[i-1] + a[i-2]
                a.pop(i)
                a.pop(i-1)
                total += len(list(combinations(a, c)))
    if n>=5:
        a = []
        d = 0
        if n == 5:
            d = 2
        else:
            d = n // 3
        for i in range(1, d+1):
            for j in range(1, n//2):
                a = []
                if (n-3*i)-(2*j)==0:
                    for k in range(i):
                        a.append(int(3))
                    for k in range(j):
                        a.append(int(2))
                    total += len(list(combinations(a, i)))
                elif (n-3*i)-(2*j)>=0:
                    if n>=6:
                        a=[]
                        for k in range(i):
                            a.append(int(3))
                        for k in range(j):
                            a.append(int(2))
                        for k in range((n-3*i)-(2*j)):
                            a.append(int(1))
                        tmp1 = len(list(combinations(a, i)))

                        a=[]
                        for k in range(j):
                            a.append(int(2))
                        for k in range((n-3*i)-(2*j)):
                            a.append(int(1))
                        tmp2 = len(list(combinations(a, j)))
                        len(list(combinations(a, j)))
                        total += tmp1*tmp2
    return total

b=[]
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    b.append(plus123(int(sys.stdin.readline().rstrip())))

for i in b:
    print(i)