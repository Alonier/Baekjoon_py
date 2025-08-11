import sys
rep = int(input())

number_arr = [ 0 for i in range(1,21)]

for i in range(rep):
    arr = sys.stdin.readline().split()
    if arr[0] == "add":
        number_arr[int(arr[1])-1] = 1
    elif arr[0] == "remove":
        number_arr[int(arr[1])-1] = 0
    elif arr[0] == "check":
        print(number_arr[int(arr[1])-1])
    elif arr[0] == "toggle":
        number_arr[int(arr[1])-1] = 1 if number_arr[int(arr[1])-1] == 0 else 0
    elif arr[0] == "all":
        number_arr = [ 1 for i in range(1,21)]
    elif arr[0] == "empty":
        number_arr = [ 0 for i in range(1,21)]
