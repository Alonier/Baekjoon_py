N = int(input())
num_N = list(map(int, input().split()))
M = int(input())
num_M = list(map(int, input().split()))

num_arr = [0 for i in range(0, 20000001)]

for i in num_N:
    num_arr[i+10000000] +=1

num_N.sort()

for M in num_M:
    left = 0
    right = N-1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if M > num_N[mid]:
            left = mid+1
        elif M < num_N[mid]:
            right = mid-1
        elif M == num_N[mid]:
            flag = True
            print(num_arr[M+10000000])
            break
    if flag == False:
        print("0")

