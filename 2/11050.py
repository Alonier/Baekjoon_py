import math
N,K = map(int, input().split())

print(1) if K == 0 else print(math.comb(N,K))
