import collections, sys
rep = int(input())
stk = collections.deque()
for i in range(rep):
    arr = sys.stdin.readline().rstrip().split()
    if len(arr)==2:
        stk.append(arr[1])
    else:
        if arr[0]=="pop":
            if len(stk)==0:
                print(-1)
            else:
                print(stk.popleft())
        elif arr[0]=="size":
            print(len(stk))
        elif arr[0]=="empty":
            if len(stk)==0:
                print(1)
            else:
                print(0)
        elif arr[0]=="front":
            if len(stk)==0:
                print(-1)
            else:
                print(stk[0])
        elif arr[0]=="back":
            if len(stk)==0:
                print(-1)
            else:
                print(stk[len(stk)-1])