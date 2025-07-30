N, M = map(int, input().split())
# N: 주어진 카드의 수, M: 최대값

a = list(map(int, input().split()))
a.sort(reverse=True)

max_ = 0

for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            sum_ = a[i]+a[j]+a[k]
            if(sum_ > M):
                continue
            if(max_ < sum_):
                max_ = sum_
print(max_)