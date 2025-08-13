T = int(input())
_arr = [0,1,1,1,2,2,3,4,5,7,9]
tmp = [0 for i in range(0, 100)]
_arr += tmp
for i in range(T):
    n = int(input())
    if n <= 10:
        print(_arr[n])
    else:
        for i in range(11, n+1):
            _arr[i] = _arr[i-1] + _arr[i-5]
        print(_arr[i])