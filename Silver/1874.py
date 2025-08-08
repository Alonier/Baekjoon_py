import collections, sys
n = int(input())

stk = collections.deque()
list_ = []

p = int(sys.stdin.readline().rstrip())
for i in range(1, n+1):
    stk.append(i)
    list_.append("+")
    while len(stk) > 0 and stk[len(stk)-1] == p:
        stk.pop()
        list_.append("-")
        try:
            p = int(sys.stdin.readline().rstrip())
        except:
            break
if len(stk) > 0:
    print("NO")
else:
    for i in list_:
        print(i)
