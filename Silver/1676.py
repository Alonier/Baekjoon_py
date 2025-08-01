import math
N = int(input())
i = str(math.factorial(N))
res = 0
for j in range(len(i),0,-1):
    if i[j-1]!="0":
        break
    res+=1

print(res)