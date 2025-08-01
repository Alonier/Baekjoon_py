import sys
rep = int(input())
a = [[] for _ in range(50)]

for i in range(rep):
    b = sys.stdin.readline().rstrip()
    # print(len(b))
    a[len(b)-1].append(b)

for i in range(50):
    if len(a[i])>0:
        tmp = list(set(a[i]))
        tmp.sort()
        for j in range(len(tmp)):
            print(tmp[j])
        