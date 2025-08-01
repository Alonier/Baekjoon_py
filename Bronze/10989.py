import sys
a = [0] * 10001

rep = int(sys.stdin.readline().rstrip())
for i in range(rep):
    a[int(sys.stdin.readline().rstrip())] += 1

for i in range(1,10001):
    if a[i]!= 0:
        for j in range(a[i]):
            print(i)
