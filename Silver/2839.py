N = int(input())

flag = False
for i in range(N//5, -1,-1):
    tmp = N
    tmp = N - i*5
    if tmp % 3 == 0:
        print(i + tmp//3)
        flag = True
        break
if flag == False:
    print(-1)
    