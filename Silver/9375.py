import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    cl = dict()
    n = int(sys.stdin.readline().rstrip())
    cnt = 1
    for i in range(n):
        # 가진 의상의 수
        cl_name, cl_kind = sys.stdin.readline().rstrip().split()
        # 의상의 이름, 의상의 종류
        if cl.get(cl_kind) == None:
            cl[cl_kind] = [cl_name]
        else:
            tmp = cl.get(cl_kind)
            tmp.append(cl_name)
            cl[cl_kind] = tmp

    for i in cl.keys():
        cnt *= (len(cl.get(i))+1)
    print(cnt-1)