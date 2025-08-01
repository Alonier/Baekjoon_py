rep = int(input())

sum = 0

def cal(k,n):
    if k==0:
        return n
    if n==1:
        return 1
    return cal(k-1,n)+cal(k,n-1)

for i in range(rep):
    k = int(input())
    # 층수
    n = int(input())
    # 호수
    sum = cal(k,n)
    print(sum)
