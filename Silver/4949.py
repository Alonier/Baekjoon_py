import collections

while(1):
    arr = input()
    if(arr == "."):
        break
    stk = collections.deque()
    flag = True
    for i in range(len(arr)-1):
        if arr[i] == '[' or arr[i] =='(':
            stk.appendleft(arr[i])
        elif arr[i] == ']':
            if len(stk)==0:
                flag = False
                break
            elif stk[0] == '[':
                stk.popleft()
            else:
                flag = False
                break
        elif arr[i] == ')':
            if len(stk)==0:
                flag = False
                break
            if stk[0] == '(':
                stk.popleft()
            else:
                flag = False
                break
    if len(stk)!= 0:
        flag = False
    print("yes") if flag == True else print("no")