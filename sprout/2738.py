n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

for i in range(n):
    tmp = list(map(int, input().split()))
    b.append(tmp)

for i in range(0,n):
    for j in range(0,m):
        tmp = a[i][j] + b[i][j]
        print(tmp, end=" ")
    print()

