rep = int(input())

for i in range(rep):
    sum = 0
    con = 1
    a = input()
    for j in range(len(a)):
        if a[j] == "O":
            sum = sum + con
            con +=1
        else:
            con = 1
    print(sum)