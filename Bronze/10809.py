list_ = []
for i in range(26):
    list_.append(-1)

a = input()
for i in range(len(a)):
    list_[ord(a[i])-97] = i if list_[ord(a[i])-97] == -1 else list_[ord(a[i])-97]

for i in range(len(list_)):
    print(list_[i], end=" ")