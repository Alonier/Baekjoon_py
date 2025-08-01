import sys
a = [False] * 2000001
# -1000000 ~ -1 : 0 - 999999
# 0: 1000000
# 1 - 1000000: 1000001 - 2000000
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    # 음의 정수에 대해서 고려
    if tmp < 0:
        a[tmp+1000000] = True
    elif tmp == 0:
        a[1000000] = True
    else:
        a[tmp+1000000] = True
        

for i in range(2000001):
    if a[i]== 1:
        if i<1000000:
            print(i-1000000)
        elif i ==1000000:
            print(0)
        else:
            print(i-1000000)