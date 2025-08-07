import collections, sys
K = int(input())
stk = collections.deque()
sum = 0
for i in range(K):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        stk.popleft()
    else:
        stk.appendleft(number)

for i in stk:
    sum += i

print(sum)