while True:
    try:
        a, b =map(int,input().split())
        print(a+b)
    except:
        break
# 오류가 발생했을 때, 캐치해서 반복문을 종료