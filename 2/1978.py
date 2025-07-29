rep = int(input())
a = list(map(int, input().split()))
sum = 0
for i in range(rep):
    flag = True
    if a[i] == 1:
        continue
    for j in range(2,1001):
        if(a[i] % j == 0):
            if(j == a[i]):
                continue
                # 자기 자신인 경우 배제
            if(j > a[i]):
                break
            flag = False
    if(flag):
        sum += 1
print(sum)