for i in range(3):
    a = list(map(int, input().split()))
    if sum(a)==4:
        print('E')
    elif sum(a)==3:
        print('A')
    elif sum(a)==2:
        print('B')
    elif sum(a)==1:
        print('C')
    else:
        print('D')
