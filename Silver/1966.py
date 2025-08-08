import sys, collections
rep = int(input())

for i in range(rep):
    N, M = map(int,sys.stdin.readline().rstrip().split())
    # N : 문서의 개수, M: 궁금한 문서의 인덱스(0~N)
    input_ = list(map(int, sys.stdin.readline().split()))
    
    if N == 1:
        print(1)
    else:
        que = collections.deque()
        for i in range(len(input_)):
            que.append([input_[i],i])
            res = 1
        while len(que) > 0:
            for ele in que:
                if ele[0] > que[0][0]:
                    que.append(que.popleft())
                    break
            else:
                num = que.popleft()
                if num[1] == M:
                    print(res)
                    break
                else:
                    res +=1