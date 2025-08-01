a = int(input())
b = int(input())
c = int(input())

sum = a*b*c

for i in range(10):
    print(str(sum).count(str(i)))