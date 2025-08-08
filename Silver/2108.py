import math, sys

def rounding(number):
    return int(number//1 + 1) if number%1 == 0.5 else round(number)

rep = int(input())
number_list = []
count = dict()

for i in range(rep):
    input_number = int(sys.stdin.readline())
    number_list.append(input_number)

    if input_number not in count:
        count[input_number] = 1
    else:
        count[input_number] +=1

if rep == 1:
    print(number_list[0])
    print(number_list[0])
    print(number_list[0])
    print(0)

else:    
    number_list.sort()
    print(rounding(sum(number_list)/rep))

    print(number_list[rep//2])

    freq = max(count.values())
    numbers = []
    for key,value in count.items():
        if value == freq:
            numbers.append(key)
    
    print(numbers[0]) if len(numbers) == 1 else print(sorted(numbers)[1])

    print(max(number_list) - min(number_list))