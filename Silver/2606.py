import sys
N = int(input())
# N: 컴퓨터의 수
M = int(input())
# M: 연결되어있는 컴퓨터 쌍의 수

visited = [False for i in range(N+1)]
visited[1] = True

computer_links = dict()
for i in range(M):
    a,b = list(map(int, sys.stdin.readline().rstrip().split()))
    if computer_links.get(a) == None:
        computer_links[a] = [b]
    else:
        tmp = computer_links.get(a)
        tmp.append(b)
        computer_links[a] = tmp
    if computer_links.get(b) == None:
        computer_links[b] = [a]
    else:
        tmp = computer_links.get(b)
        tmp.append(a)
        computer_links[b] = tmp
        
def DFS(a):
    if computer_links.get(a) == None:
        return
    _arr = computer_links.get(a)
    for i in _arr:
        if visited[i] == False:
            visited[i] = True
            # print("visit" , i)
            DFS(i)

DFS(1)
sum = 0
for i in visited:
    if i == True:
        sum+=1
    
print(sum-1)
