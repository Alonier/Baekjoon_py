rep = int(input())
stu_list = []
for i in range(rep):
    stu_list.append(list(map(int, input().split())))

for i in range(len(stu_list)):
    rank = 1
    for j in range(len(stu_list)):
        if stu_list[j][0] > stu_list[i][0] and stu_list[j][1] > stu_list[i][1]:
            rank += 1
    print(rank, end = " ")