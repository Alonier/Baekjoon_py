min = 1000001
max = -1000001

rep = int(input())
a = list(map(int, input().split()))
for i in range(rep):
    if(a[i] > max):
        max = a[i]
    if(a[i] < min):
        min = a[i]

print(min, max)