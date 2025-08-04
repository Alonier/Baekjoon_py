rep = int(input())
mem_list = []

for i in range(rep):
    member = list(input().split())
    mem_list.append([int(member[0]), member[1]])

mem_list.sort(key = lambda x : x[0])

for i in mem_list:
    print(i[0], i[1])