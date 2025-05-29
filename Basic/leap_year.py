a = int(input())
if (a%4==0 and a%100!=0) or a%400==0: ##여기서 &&는 없으며 &는 비트 연산자
    print(1)
else:
    print(0)
