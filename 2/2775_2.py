rep = int(input())

for i in range(rep):
    k = int(input())
    n = int(input())
    
    l = []
    for j in range(0,k+1):
        p = []
        for m in range(0,n):
            if j==0:
                p.append(m+1)
            elif m==0:
                p.append(1)
            else:
                p.append(l[j-1][m] + p[m-1])
        l.append(p)
    print(l[k][n-1])
    
    
