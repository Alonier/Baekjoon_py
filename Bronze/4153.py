while(1):
    tmp = input()
    if(tmp == "0 0 0"):
        break
    a = list(map(int,tmp.split()))
    a.sort()
    if(a[0]*a[0] + a[1]*a[1] == a[2]*a[2]):
        print("right")
    else:
        print("wrong")