a, b = map(int, input().split())
c = a*b

if a < b:
    tmp = a
    a = b
    b = tmp

while(1):
    if a%b==0:
        break
    tmp = a%b
    a=b
    b=tmp

print(b)
print(int(c/b))