import sys
N, K = map(int, input().split())
# N: 가진 동전의 종류, K는 만들고 싶은 가치
# 목적: 동전개수의 최소값

def calculate(arr, goal):
    res = 0
    for i in arr:
        res += goal // i
        goal = goal % i
    return res

coin = []

for i in range(N):
    money = int(sys.stdin.readline().rstrip())
    if money <= K:
        coin.append(money)

coin.sort(reverse=True)

print(calculate(coin, K))

