import math
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
# T는 티셔츠 묶음, P는 펜의 묶음
sum = 0

for i in range(len(size)):
    sum += math.ceil(size[i]/T)

print(sum)
print(math.floor(N/P), N%P)
# 펜의 묶음 수와 한자루 수
