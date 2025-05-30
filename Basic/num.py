a, b = map(int, input().split())

if b==a:
    print(0)
    exit()
elif b>a:
    print(b-a-1)
    for i in range(a+1,b):
        print(i, end=" ")
else:
    print(a-b-1)
    for i in range(b+1,a):
        print(i, end=" ")
