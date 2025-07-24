import sys

rep = int(sys.stdin.readline())

for i in range(rep):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a + b)