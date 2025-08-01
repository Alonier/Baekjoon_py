import math
rep = int(input())

for i in range(rep):
    H, W, N = map(int, input().split())
    floor = H if N % H == 0 else N%H 
    num = math.ceil(N / H)
    num = "0"+str(num) if num < 10 else str(num)
    print(str(floor) + num)