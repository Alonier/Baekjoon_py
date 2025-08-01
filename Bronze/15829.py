L = int(input())
a = input()
sum = 0

for i in range(L):
    sum = sum + (ord(a[i]) - 96) * pow(31, i)

print(sum%1234567891)
