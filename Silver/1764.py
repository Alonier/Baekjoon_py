import sys
N, M = map(int, input().split())
# N: 듣도 못한 사람의 수, M: 보도 못한 사람의 수

no_listen = dict()
arr = []

for i in range(N):
    _input = sys.stdin.readline().rstrip()
    no_listen[_input] = 1

for i in range(M):
    _input = sys.stdin.readline().rstrip()
    if no_listen.get(_input) == None:
        continue
    else:
        arr.append(_input)

print(len(arr))
arr.sort()
for i in range(len(arr)):
    print(arr[i])
