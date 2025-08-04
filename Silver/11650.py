import sys
rep = int(input())
list_ = []
for i in range(rep):
    list_.append(list(map(int,sys.stdin.readline().rstrip().split())))
list_.sort(key=lambda x: (x[0],x[1]))
for i in list_:
    print(i[0],i[1])