N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int,input().split()))

a.sort()

for m in b:
    start = 0
    end = N-1
    flag = False

    while start <= end:
        p = (start + end) // 2
        if m > a[p]:
            start = p + 1
        elif m < a[p]:
            end = p - 1
        else:
            flag = True
            break
    print(1) if flag == True else print(0)
        