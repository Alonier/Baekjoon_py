import math, sys
n = int(sys.stdin.readline().rstrip())

dp = [0] * (n+1)

for i in range(1, n+1):
    if pow(i,0.5).is_integer():
        dp[i] = 1
    j = 1
    while j*j <= i:
        if dp[i] == 0:
            dp[i] = dp[j*j] + dp[i - j*j]
        else:
            dp[i] = min(dp[i], dp[j*j] + dp[i - j*j])
        j+=1

print(dp[n])

