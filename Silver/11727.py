n = int(input())

dp = [0 for i in range(0,1000)]

dp[0] = 1
# 1번째
dp[1] = 3
# 2번째

if(n > 2):
    for i in range(2,n):
        dp[i] = (2 * dp[i-2]) + dp[i-1]

print(dp[n-1] % 10007)