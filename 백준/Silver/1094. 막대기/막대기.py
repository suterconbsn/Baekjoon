x=int(input())
stick = 64
sticklist = []
condition = 1 
count = 0 

if x == 64 or x == 1:
    sticklist.append(x)
    condition = 0

while condition:
    stick /= 2

    if stick <= x:
        sticklist.append(stick)
        x -= stick
        if x == 0:
            condition = 0

for i in sticklist:
    count += 1

print(count)
