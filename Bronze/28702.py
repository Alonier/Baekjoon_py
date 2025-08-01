a = 0
point = 0
for i in range(3):
    try:
        a = int(input())
        point = i
    except:
        continue
nt = a+3-point
print("FizzBuzz") if (nt%3 == 0)and(nt%5==0) else print("Fizz") if nt%3==0 else print("Buzz") if nt%5==0 else print(nt)