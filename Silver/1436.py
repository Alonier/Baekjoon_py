N = int(input())
i = 0
j = 666

while(1):
    if str(j).find("666")!= -1:
        i +=1
    if i==N:
        break
    j+=1
print(j)