N = int(input())
num_N = list(map(int, input().split()))
M = int(input())
num_M = list(map(int, input().split()))

num_arr = [0 for i in range(0, 20000001)]

for i in num_N:
    num_arr[i+10000000] +=1

for M in num_M:
    print(num_arr[M+10000000])

