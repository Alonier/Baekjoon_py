a = input()
sum = 0
point = 0

for i in range(len(a)):
    if a[i] == "*":
        point = i
    else:
        if i%2 == 0:
            sum += int(a[i])
        else:
            sum += 3*int(a[i])

lt = str(sum)
# print(sum)
if point%2 == 0:
    print(10 - int(lt[len(lt)-1]))
    # 이거는 무조건 맞음
else:
    for i in range(10):
        if (sum + 3*i)%10 == 0:
            print(i)
    # 이거는 무조건 틀림
    # 20 혹은 30으로 나머지 0을 만드는걸 고려하지 않음