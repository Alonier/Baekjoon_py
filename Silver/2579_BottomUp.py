import sys
rep = int(sys.stdin.readline().rstrip())

d = [[0,0] for i in range(rep + 1)]

stair_point = dict()
stepped = dict()
for i in range(rep):
    stair_point[i] = int(sys.stdin.readline().rstrip())

d[1][0] = stair_point[0]
d[1][1] = stair_point[0]

for i in range(2, rep+1):
    d[i][1] = d[i-1][0] + stair_point[i-1]
    # 한 계단 씩
    d[i][0] = max(d[i-2][1], d[i-2][0]) + stair_point[i-1]
    # 두 계단 씩

print(max(d[rep][0],d[rep][1]))
