import sys

n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

v = int(sys.stdin.readline().rstrip())

sum = 0

for i in range(n):
    if(arr[i] == v):
        sum += 1

print(sum)