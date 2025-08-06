import collections

rep = int(input())

for i in range(rep):
    stk = collections.deque()
    arr = input()
    flag = True
    for j in range(len(arr)):
        if arr[j] == '(':
            stk.appendleft(arr[j])
        else:
            if len(stk) == 0:
                flag = False
                break
            if stk[0] == '(':
                stk.popleft()
            else:
                flag = False
                break
    if len(stk)!= 0:
        flag = False
    print("YES") if flag == True else print("NO")