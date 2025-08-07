import collections
stk = collections.deque()
N, K = map(int, input().split())
for i in range(1, N+1):
    stk.append(i)
num = 1
print("<",end="")
while len(stk) > 1:
    if num%K == 0:
        print(stk.popleft(), end=", ")
    else:
        stk.append(stk.popleft())
    num+=1
print(stk[0], end=">")