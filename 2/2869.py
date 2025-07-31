import math
A, B, V = map(int, input().split())
# A:올라가는 높이, B: 미끄러지는 높이, V: 목표 높이
g = V-A
print(math.ceil(g/(A-B))+1)