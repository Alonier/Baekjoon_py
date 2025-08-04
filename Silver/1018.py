height, width = map(int, input().split())
map = []
res = 2501

for i in range(height):
    map.append(input())

#W Case
for i in range(height-7):
    for j in range(width-7):
        WRes = 0
        for k in range(i,i+8):
            for l in range(j,j+8):  
                if ((k+l)%2 == 0) and map[k][l] != "W":
                    WRes +=1
                elif ((k+l)%2 != 0) and map[k][l] != "B":
                    WRes +=1
        if WRes < res:
            res = WRes
        
#B Case
for i in range(height-7):
    for j in range(width-7):
        BRes = 0
        for k in range(i,i+8):
            for l in range(j,j+8):  
                if ((k+l)%2 == 0) and map[k][l] != "B":
                    BRes +=1
                elif ((k+l)%2 != 0) and map[k][l] != "W":
                    BRes +=1
        if BRes < res:
            res = BRes
        
print(res)
        