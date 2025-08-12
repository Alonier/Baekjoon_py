import sys
N, M = map(int, input().split())
# N: 저장된 사이트 주소의 수, M: 찾으려는 사이트 주소의 수

password_arr = dict()
for i in range(N):
    site_domain, password = sys.stdin.readline().rstrip().split()
    password_arr[site_domain] = password

for i in range(M):
    site_domain = sys.stdin.readline().rstrip()
    print(password_arr.get(site_domain))