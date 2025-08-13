import sys, collections
N, M = map(int, input().split())

a = list(map(int, input().split()))
sum_list = [0 for i in range(N+1)]
sum_list[0] = 0
sum_list[1] = a[0]


for i in range(0,N):
    sum_list[i+1] = a[i] + sum_list[i]

for l in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(sum_list[j] - sum_list[i-1])