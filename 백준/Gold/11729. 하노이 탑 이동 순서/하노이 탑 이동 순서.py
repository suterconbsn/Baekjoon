n = int(input())
a = []
count = 0
def move(n, x, y):
    global count
    if n>1:
        move(n-1, x, 6-x-y)
    a.append(f'{x} {y}')
    count += 1
    if n>1:
        move(n-1, 6-x-y, y)

move(n, 1, 3)
print(count)
for i in a:
    print(i)