import math

while(1):
    a = input()
    if(a == "0"):
        break
    l = math.floor(len(a)/2)
    flag = True
    for i in range(l):
        # print(a[i], a[len(a)-i-1])
        if a[i] != a[len(a)-i-1]:
            flag = False
            break
    print("yes") if flag else print("no")