rep = int(input())
for i in range(rep):
    m, str_ = input().split()
    for j in range(len(str_)):
        for k in range(int(m)):
            print(str_[j], end="")
    print()