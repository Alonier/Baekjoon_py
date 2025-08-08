import sys, collections

def rounding(number):
    int_ = int(number//1)
    return int_ + 1 if number%1 == 0.5 else round(number)

rep = int(input())
exclude = rounding(rep*0.15)
stk = collections.deque()
level = [0 for i in range(30)]
for i in range(rep):
    input_ = int(sys.stdin.readline())
    level[input_-1] +=1
for i in range(30):
    for j in range(level[i]):
        stk.append(i+1)
for i in range(exclude):
    stk.popleft()
    stk.pop()
sum = 0
length = len(stk)
for i in range(length):
    sum += stk.pop()
if length == 0:
    print(0)
else:
    res = sum/length
    print(rounding(res))


