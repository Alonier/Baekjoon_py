a = int(input())
sum = 0
cnt = 1
num = 1

while(1):
    sum += num
    if(a <= sum):
        break
    num = cnt*6
    cnt += 1

print(cnt)