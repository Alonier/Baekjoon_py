import sys
N, M = map(int, input().split())
# N: 도감에 수록된 포켓몬의 개수, M: 내가 맞춰야하는 문제의 개수
# 2-N+1까지 1-N에 해당하는 포켓몬을 입력
# 다음 줄 부터는 맞추어야하는 문제
# 알파벳으로 들어오면 번호, 번호로 들어오면 알파벳을 출력

number_to_name = dict()
name_to_number = dict()
arr = []
for i in range(N):
    pokemon_name = sys.stdin.readline().rstrip()
    number_to_name[i+1] = pokemon_name
    name_to_number[pokemon_name] = i+1

for i in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        arr.append(number_to_name.get(int(question)))
    else:
        arr.append(name_to_number.get(question))


for i in range(len(arr)):
    print(arr[i])