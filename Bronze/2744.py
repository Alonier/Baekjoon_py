tmp = input()
res = ''

for i in range(len(tmp)):
    if(tmp[i].islower()):
        res += tmp[i].upper()
    else:
        res += tmp[i].lower()

print(res)
#파이썬 문자열은 불변객체