rep = int(input())

a = list(map(int, input().split()))
a.sort(reverse=True)
sum = 0

for i in range(0,len(a)):
    sum += a[i]/a[0]*100

print(sum/rep)