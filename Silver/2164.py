import collections
M = int(input())

a = collections.deque([i for i in range(1,M+1)])

tmp = 0
while len(a) > 1:
    if tmp%2 == 0:
            a.popleft()
    else:
            a.append(a.popleft())
    tmp+=1
print(a.popleft())