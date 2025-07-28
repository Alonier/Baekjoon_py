rep = int(input())
for i in range(rep):
    a = input()
    print(a+a) if len(a)==0 else print(a[0]+a[len(a)-1])