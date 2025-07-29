n = int(input())

for i in range(1, n+1):
    num = sum(map(int, str(i)))
    num_sum = num + i
    if(n == num_sum):
        print(i)
        break
    if(i == n):
        print(0)