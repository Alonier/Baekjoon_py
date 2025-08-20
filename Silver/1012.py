import sys, collections
T = int(input())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    _map = [[0 for i in range(M)] for i in range(N)]
    for i in range(K):
        x,y = map(int, sys.stdin.readline().rstrip().split())
        _map[y][x] = 1
    stk = collections.deque()
    res = 0
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 1:
                stk.appendleft([i,j])
                _map[i][j] = 0
                while(1):
                    if len(stk) == 0:
                        res+=1
                        break
                    tmp = stk.popleft()
                    k = tmp[0]
                    m = tmp[1]
                    # 좌측탐색
                    if m != 0 and _map[k][m-1] == 1:
                        _map[k][m-1] = 0
                        stk.appendleft([k,m-1])
                    # 우측탐색
                    if m != M-1 and _map[k][m+1] == 1:
                        _map[k][m+1] = 0
                        stk.appendleft([k,m+1])
                    # 하측탐색
                    if k != N-1 and _map[k+1][m] == 1:
                        _map[k+1][m] = 0
                        stk.appendleft([k+1,m])
                    # 상측탐색
                    if k != 0 and _map[k-1][m] == 1:
                        _map[k-1][m] = 0
                        stk.appendleft([k-1,m])
                    
    print(res)
                

        