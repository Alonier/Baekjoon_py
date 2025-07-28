import sys

a = []
b = []

for i in range(28):
    a.append(int(sys.stdin.readline().rstrip()))

for i in range(1, 31):
    try:
        a.index(i)
    except:
        b.append(i)
        continue  

b.sort(reverse=True)

print(b.pop())
print(b.pop())