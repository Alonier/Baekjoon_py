n = int(input())
_arr = [0 for i in range(1000)]
_arr[0] = 1
_arr[1] = 2
for i in range(2,n):
    _arr[i] = _arr[i-2] + _arr[i-1]

print(_arr[n-1] % 10007)