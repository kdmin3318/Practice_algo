n = [int(input()) for i in range(9)]
t = sum(n) - 100
n.sort()
for i in range(8):
    for j in range(i+1,9):
        if n[i]+n[j]==t:
            n.pop(j)
            n.pop(i)
            for k in range(7):
                print(n[k])
            exit()
