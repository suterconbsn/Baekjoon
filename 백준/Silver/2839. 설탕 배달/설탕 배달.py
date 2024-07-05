import sys

n=int(sys.stdin.readline().rstrip())

def sugar(n):
    a = int(n / 5)
    if n == 3:
        return 1
    if n % 5 == 0:
        return n // 5
    while a > -1:
        if (n-a*5) % 3 == 0:
            return a+(n-a*5)//3
        a-=1
    return -1

print(sugar(n))
