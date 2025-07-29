rep = int(input())
a = list(map(int, input().split()))
sum = 0

for i in range(rep):
    flag = True
    if(a[i] == 1):
        continue
    for j in range(2, a[i]):
        if a[i] % j == 0:
            flag = False
    if(flag):
        sum += 1

print(sum)