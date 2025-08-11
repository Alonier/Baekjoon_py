N = int(input())
# 사람의 수

a = list(map(int,input().split()))
a.sort()
sum = 0
tmp = 0
for i in a:
    tmp += i
    sum += tmp
print(sum)